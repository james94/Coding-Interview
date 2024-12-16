#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <chrono>
#include <algorithm>
#include <thread>

class Database {
    struct Entry {
        std::string value;
        std::chrono::system_clock::time_point expiry;
    };

    std::unordered_map<std::string, Entry> data;

public:
    void set(const std::string& key, const std::string& value, int ttl_seconds = -1) {
        auto expiry = (ttl_seconds == -1) ? std::chrono::system_clock::time_point() : std::chrono::system_clock::now() + std::chrono::seconds(ttl_seconds);
        data[key] = {value, expiry};
    }

    std::string get(const std::string& key) {
        auto it = data.find(key);
        if (it != data.end()) {
            if (it->second.expiry > std::chrono::system_clock::now() || it->second.expiry == std::chrono::system_clock::time_point()) {
                return it->second.value;
            }
            data.erase(it);
        }
        return "";
    }

    void remove(const std::string& key) {
        data.erase(key);
    }

    std::vector<std::string> find(const std::string& prefix) {
        std::vector<std::string> results;
        for (const auto& [key, entry] : data) {
            if (key.compare(0, prefix.length(), prefix) == 0) {
                if (entry.expiry > std::chrono::system_clock::now() || entry.expiry == std::chrono::system_clock::time_point()) {
                    results.push_back(key);
                }
            }
        }
        std::sort(results.begin(), results.end());
        return results;
    }

    // New method for batch operations, relevant for financial data processing
    void batchSet(const std::vector<std::pair<std::string, std::string>>& entries, int ttl_seconds = -1) {
        for (const auto& [key, value] : entries) {
            set(key, value, ttl_seconds);
        }
    }
};

int main() {
    Database db;

    // Simulating financial operations
    db.set("transaction:001", "Amount: $500, Type: Corporate Card, Vendor: Office Suppliers Inc.", 3600);

    db.set("transaction:002", "Amount: $1000, Type: Bill Payment, Vendor: Electricity Company", 3600);

    db.set("vedor:001", "Name: Office Supplies Inc., Payment Terms: Net 30", -1);

    // Demonstrating batch operations
    std::vector<std::pair<std::string, std::string>> batch_entries = {
        {"expense:001", "Employee: John Doe, Amount: $150, Category: Travel"},
        {"expense:002", "Employee: Jane Smith, Amount: $75, Category: Meals"}
    };
    db.batchSet(batch_entries, 86400); // Set TTL for 24 hours

    // Retrieving and displaying data
    std::cout << "Transaction 001: " << db.get("transaction:001") << std::endl;
    std::cout << "Vendor 001: " << db.get("vendor:001") << std::endl;

    // Demonstrating prefix search
    std::cout << "All expenses: " << std::endl;
    for (const auto& key : db.find("expense:")) {
        std::cout << key << ": " << db.get(key) << std::endl;
    }

    // Simulating time passage and TTL expiration
    std::this_thread::sleep_for(std::chrono::seconds(4));
    std::cout << "After 4 seconds, Transaction 001: " << db.get("transaction:001") << std::endl;

    return 0;
}

# LRU Cache

**Medium**

**Companies:** Amazon: 67, Bloomberg: 21, Microsoft: 19, Facebook: 15, Apple: 14, Oracle: 11, Google, Twilio, Asana, VMware, Uber, Cruise Automation, Yahoo, Two Sigma, Dropbox, Salesforce, Expedia, Yandex, Citadel, Snapchat, Zillow, Spotify, ByteDance, Cisco, Adobe, LinkedIn, Paypal, Cloudera, TripAdvisor, Nutanix

Design and implement a data structure for **Least Recently Used (LRU) cache**. It should support the following operations: get and put.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a **positive** capacity.

Follow up:
Could you do both operations in **O(1)** time complexity?

**Example:**

~~~
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
~~~

## Solution

### C++

### Approach 1: Hash Map STL

Runtime: **148 ms**

Memory Usage: **37.9 MB**

~~~cpp
#include <unordered_map>
using namespace std;

class LRUCache {
private:
    int time;
    int cap;
    unordered_map<int, int>kv_map, kt_map;
public:
    LRUCache(int capacity) {
        time = 0;
        cap = capacity;
    }
    
    int get(int key) {
        // check is key not present
        if(kv_map.find(key) == kv_map.end())
        {
            return -1;
        }
        
        // update time at which key was used at
        kt_map[key] = time++;
        
        // get value from key
        return kv_map[key];
    }
    
    void put(int key, int value) {
        // Evict if new key not present and capacity full
        if(kv_map.find(key) == kv_map.end() && kv_map.size() == cap)
        {
            int min_time = INT_MAX;
            int min_key = -1;
            for(auto it = kt_map.begin(); it != kt_map.end(); it++)
            {
                // find key least recently used based on lowest time
                if(it->second < min_time)
                {
                    min_time = it->second;
                    min_key = it->first;
                }
            }
            // erase least recently used key:value
            kv_map.erase(min_key);
            kt_map.erase(min_key);
        }
        
        // insert new item 
        kv_map[key] = value;
        // update time at which key was used at
        kt_map[key] = time++;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
~~~

**Complexity Analysis**

Time Complexity: O(1) for `get` since all operations are done in constant time and O(n) for `put` since iteration is used to find key least recently used.

Space Complexity: O(capacity) since the space is used only for 2 hash maps with at most `capacity + 1` elements.

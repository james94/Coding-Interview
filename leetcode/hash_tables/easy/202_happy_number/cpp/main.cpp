// Time: 7:31PM - 10:17PM (with headache):

#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
#include <unordered_map>

// 202. Happy Number
// Leetcode Ref: https://leetcode.com/problems/happy-number/description/?envType=company&envId=google&favoriteSlug=google-all&difficulty=EASY
// Hash Table, Math, Two Pointers

// Determine if number `n` is happy
// A "happy number" is a number defined by:

// - Starting with any positive integer, replace
// number by sum of squares of its digits

// - Repeat process until the number equals 1
// (where it will stay), or it loops endlessly
// in a cycle which does not include 1

// - Those numbers for which this process
// ends in 1 are happy

bool HappyNumber(int num) {
    int input_num = num;
    bool happy = false;

    if (num == 1) {
        happy = true;
        return happy;
    }

    if (num < 0) {
        happy = false;
        return happy;
    }

    int i = 0;
    while(true) {
        std::string num_str = std::to_string(input_num);
        int sum_of_sqs_res = 0;
        std::cout << "Do Sum of Sqs: " << num_str << "\n";

        std::for_each(std::begin(num_str), std::end(num_str), [&sum_of_sqs_res](char digit_str) {
            std::cout << "[" << digit_str << "]\n";
            const int digit = std::stoi(std::to_string(digit_str)) - 48;
            std::cout << "Digit Sqd: " << pow(digit, 2) << "\n";
            sum_of_sqs_res += pow(digit, 2);
        });
        std::cout << "Sum of Sqs: " << sum_of_sqs_res << "\n";
        if (sum_of_sqs_res == 1) {
            std::cout << "After " << i << " Iterations\n";
            happy = true;
            break;
        }
        else if (i > 100) {
            std::cout << "After " << i << " Iterations, Sum of Sqs != 1\n";
            happy = false;
            break;
        }
        input_num = sum_of_sqs_res;
        i++;
    }

    return happy;
}

int main() {
    int num1 = 19;
    std::string happy_num = HappyNumber(num1) ? "Happy" : "Not Happy";
    std::cout << std::to_string(num1) << ": " << happy_num << " Number\n";
    return 0;
}
# Two Sum

**Easy**

**Companies:** Amazon: 209, Google: 82, Adobe: 55, Apple: 43, Microsoft: 35, Facebook: 24, Bloomberg: 19, Yahoo: 18, Oracle, Goldman Sachs, Uber, Cisco, Expedia, Walmart Labs, ServiceNow, Huawei, Yandex, VMware, FactSet, Splunk, Alibaba, LinkedIn, Morgan Stanley, Intuit, GoDaddy, Intel, Salesforce, Tableau, Qualcomm, ByteDance

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have ***exactly*** one solution, and you may not use the same element twice.

**Example:**

~~~javascript
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
~~~

## Solution

### C++

**Approach 1: Brute Force**

The brute force approach is simple. Loop through each element x and find if there is another value that equals to _target−x_.

Runtime: 140ms

Memory Usage: 9.3MB

~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for(int i = 0; i < nums.size(); i++)
        {
            for(int j = i+1; j < nums.size(); j++)
            {
                if(nums[j] == target - nums[i])
                {
                    // indices of two elements whose sum equals target
                    result.push_back(i); // index of first element
                    result.push_back(j); // index of second element
                    return result;
                }
            }
        }
        return result;
    }
};
~~~

**Complexity Analysis:**

Time complexity : O(n^2). For each element, we try to find its complement by looping through the rest of array which takes O(n) time. Therefore, the time complexity is O(n^2).

Space complexity : O(1).

**Approach 2: Two-pass Hash Table**

To improve our run time complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.

We reduce the look up time from O(n) to O(1) by trading space for speed. A hash table is built exactly for this purpose, it supports fast look up in near constant time. I say "near" because if a collision occurred, a look up could degenerate to O(n) time. But look up in hash table should be amortized O(1) time as long as the hash function was chosen carefully.

A simple implementation uses two iterations. In the first iteration, we add each element's value and its index to the table. Then, in the second iteration we check if each element's complement (_target−nums[i]_) exists in the table. Beware that the complement must not be _nums[i]_ itself!

Runtime: 20ms

Memory Usage: 10.6MB

~~~cpp
#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // two pass hash table
        map<int, int> map;
        vector<int> result;
        
        for(int i = 0; i<nums.size(); i++)
        {
            map.insert(pair<int, int>(nums[i], i));
        }
        
        for(int i = 0; i<nums.size(); i++)
        {
            int complement = target - nums[i];
            if(map.find(complement)!=map.end() && map.find(complement)->second != i)
            {
                // indices of two elements whose sum equals target
                result.push_back(i); // index of first element
                result.push_back(map.find(complement)->second);
                return result;
            }
        }
        return result;
    }
};
~~~

**Complexity Analysis:**

Time complexity : O(n). We traverse the list containing n elements exactly twice. Since the hash table reduces the look up time to O(1), the time complexity is O(n).

Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly n elements.

**Approach 3: One-pass Hash Table**

It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.

Runtime: 8ms

Memory Usage: 10.2MB

~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // One-pass Hash Table
        map<int, int> map;
        vector<int> result;
        
        for(int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];
            if(map.find(complement)!= map.end())
            {
                // indices of two elements whose sum equals target
                result.push_back(i); // index of first element
                result.push_back(map.find(complement)->second);
                return result;
            }
            map.insert(pair<int, int>(nums[i], i));
        }
        
        return result;
    }
};
~~~

**Complexity Analysis:**

Time complexity : O(n). We traverse the list containing nn elements only once. Each look up in the table costs only O(1) time.

Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores at most n elements.

## Further Reading

- [Map in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/map-associative-containers-the-c-standard-template-library-stl/)
- [How to check if a given key exists in a Map | C++](https://thispointer.com/how-check-if-a-given-key-exists-in-a-map-c/)
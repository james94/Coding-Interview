# Add Strings

**Easy**

_Companies_: ***0-6 months:*** Facebook: 25, Oracle: 8, Microsoft: 2, Snapchat: 2, Amazon: 2; ***6 months - 1 year:*** Adobe: 3, Google: 2, Square: 2, Bloomberg: 2; ***1 year - 2 years:*** Apple: 2, Alibaba: 2, Nvidia: 2, ByteDance: 2, Airbnb

_Related Topics_: String

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

1. The length of both num1 and num2 is < 5100.
2. Both num1 and num2 contains only digits 0-9.
3. Both num1 and num2 does not contain any leading zero.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

## Solution

### C++

### Approach 1: Brute Force

We traverse both strings num1 and num2. We take each char element from string num1 and num2, pass it into a hash map as a char key, get back the equivalent integer value, then add each value to the sum. We take the sum integer and convert it to a string, then add it to the result string. Finally, at the end of the loop, we calculate the carry. Then repeat the loop until the sum has been computed.

Runtime: **24 ms**

Memory Usage: **58.2 MB**

**C++ Code**

~~~cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        string res = "";
        
        map<char, int> mp{{'0', 0}, {'1', 1}, {'2', 2}, {'3', 3}, {'4', 4},
                          {'5', 5}, {'6', 6}, {'7', 7}, {'8', 8}, {'9', 9}};
        
        int i = num1.size() - 1, j = num2.size() - 1;
        
        int carry = 0;        
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            if (i>=0) {
                sum += mp[num1[i]];
                i--;
            }
            
            if (j>=0) {
                sum += mp[num2[j]];
                j--;
            }
            
            res = to_string( (int) sum % 10) + res;
            carry = (int) sum / 10;
        }
        
        return res;
    }
};
~~~

**Complexity Analysis**

Time Complexity: O(m+n). we traverse the string num1 containing m elements and string num2 containing n elements.

Space Complexity: O(n). the extra space is for the hash map, which holds a digit key mapped to a digit value.
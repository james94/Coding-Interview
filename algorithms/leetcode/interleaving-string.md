# Interleaving String

**Hard**

_Companies:_ ***0-6 months:*** Apple: 7, Amazon: 6, Google: 4, Bloomberg: 2; ***6 months - 1 year***: Microsoft: 3, Uber: 2; ***1-2 years:*** Aetion: 2, Nvidia: 2

Given _s1, s2, s3_, find whether _s3_ is formed by the interleaving of _s1_ and _s2_.

_Related Topics_: String, Dynamic Programming

**Example 1:**

~~~
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
~~~

**Example 2:**

~~~
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
~~~

## Solution

### C++

### Approach 1: Brute Force

> **Warning**: Heads up when running this code, I received **Time Limit Exceed**.

**Algorithm Explanation**

The most basic idea is to find every string possible by all interleavings of the two given strings s1 and s2. In order to implement this method, we are using recursion. We start by taking the current character of the first string s1 and then appending all possible interleavings of the remaining portion of the first string s1 and the second string s2 and comparing each result formed with the required interleaved string s3. Similarly, we choose one character from the second string s2 and form all the interleavings with the remaining portion of s2 and s1 to check if the required string s1 can be formed.

For implementing the recursive function, we make the function call recursively as is_Interleave(s1,i+1,s2,j,res+s1[i],s3), in which we have chosen the current character from s1 and then make another function call is_Interleave(s1,i,s2,j+1,res+s2[j],s3), in which the current character of s2 is chosen. Here, resres refers to that portion(interleaved) of s1 and s2 which has already been processed. If anyone of these calls return the result as True, it means that atleast one interleaving gives the required result s3. The recursive calls end when both the strings s1 and s2 have been fully processed.

Let's look at a small example to see how the execution proceeds.

~~~cpp
s1="abc"
s2="bcd"
s3="abcbdc"
~~~

Firstly we choose 'a' of s1 as the processed part i.e. res and call the recursive function considering the new strings as s1="bc", s2="bcd", s3="abcbdc". When this function returns a result, we again call the recursive function but with the new strings as s1="abc", s2="cd", s3="abcbdc".

**C++ Code**

~~~cpp
class Solution {
public:
    // Complexity Analysis
    // Time Complexity: O(2^(m+n)). m is the length of s1 and n is the length of s2.
    // Space Complexity: O(m+n). The size of stack for recursive calls can go up to m+n.
    
    // recursive function goes through all possible interleavings formed by s1 and s2,
    // checks if there is a formation that equals s3 in the case that there is one,
    // returns true. Otherwise, returns false
    bool bruteForceInterleave(string s1, int i, string s2, int j, string res, string s3) {
        if(res == s3 && i == s1.size() && j == s2.size()) {
            return true;
        }
        
        bool ans = false;
        
        if(i < s1.size()) {
            ans = ans | bruteForceInterleave(s1, i+1, s2, j, res+s1[i], s3);
        }
        
        if(j < s2.size()) {
            ans = ans | bruteForceInterleave(s1, i, s2, j+1, res+s2[j], s3);
        }
        return ans;
    }
    bool isInterleave(string s1, string s2, string s3) {
        return bruteForceInterleave(s1, 0, s2, 0, "", s3);
    }
};
~~~

**Complexity Analysis**

Time complexity : O(2^{m+n}). m is the length of s1 and n is the length of s2.

Space complexity : O(m+n). The size of stack for recursive calls can go upto m+n.

### Approach 2: Recursion with Memoization

> **Warning**: Heads up when running this code, I received **Time Limit Exceed**. I was able to get through 94 out of 101 test cases passed before receiving that message.

**Algorithm Explanation:**

In the recursive approach discussed above, we are considering every possible string formed by interleaving the two given strings. But, there will be cases encountered in which, the same portion of s1 and s2 would have been processed already but in different orders(permutations). But irrespective of the order of processing, if the resultant string formed till now is matching with the required string(s3), the final result is dependent only on the remaining portions of s1 and s2, but not on the already processed portion. Thus, the recursive approach leads to redundant computations.

This redundancy can be removed by making use of memoization along with recursion. For this, we maitain 3 pointers i, j, k which correspond to the index of the current character of s1, s2, s3 respectively. Also, we maintain a 2D memo array to keep a track of the substrings processed so far. memo[i][j] stores a 1/0 or -1 depending on whether the current portion of strings i.e. upto i^{th} index for s1 and upto j^{th} index for s2 has already been evaluated. Again, we start by selecting the current character of s1 (pointed by i). If it matches the current character of s3 (pointed by k), we include it in the processed string and call the same function recurively as: is_Interleave(s1,i+1,s2,j,s3,k+1,memo)

Thus, here we have called the function by incrementing the pointers i and k since the portion of strings upto those indices has already been processed. Similarly, we choose one character from the second string and continue. The recursive function ends when either of the two strings s1 or s2 has been fully processed. If, let's say, the string s1 has been fully processed, we directly compare the remaining portion of s2 with the remaining portion of s3. When the backtrack occurs from the recursive calls, we store the value returned by the recursive functions in the memoization array memo appropriatelys so that when it is encountered the next time, the recursive function won't be called, but the memoization array itself will return the previous generated result.

**C++ Code:**

~~~cpp
class Solution {
public:
    bool rMemInterleave(string s1, int i, string s2, int j, string s3, int k, vector<vector<int>> memo) {
        // has s1 been fully processed
        if(i == s1.size()) {
            // return whether remaining s2 substring equals remaining s3 substring
            return s2.substr(j) == s3.substr(k);
        }
        // have we iterated through all s2
        if(j == s2.size()) {
            // return whether remaining s1 substring equals remaining s3 substring
            return s1.substr(i) == s3.substr(k);
        }
        // check have we processed that substring already
        if(memo[i][j] >= 0) {
            return memo[i][j] == 1 ? true : false;
        }
        // select current char of s1 (pointed by i), does it match current char of s3?
        // if it matches, then we include it in the processed string and do recursion
        bool ans = false;
        if(s3[k] == s1[i] && rMemInterleave(s1, i+1, s2, j, s3, k+1, memo)
          || s3[k] == s2[j] && rMemInterleave(s1, i, s2, j+1, s3, k+1, memo)) {
            ans = true;
        }
        // backtrack occurs from recursive calls, store the value returned by
        // the recursive functions in the memoization array memo appropriately
        // so, when it is encountered next time, the recursive function won't
        // be called, but the memoization array itself will return previous result
        memo[i][j] = ans ? 1 : 0;
        return ans;
    }
    bool isInterleave(string s1, string s2, string s3) {
        // maintain 2D memo array to keep track of substrings processed so far
        // stores 1/0 or -1 depending on whether current portion of strings upto
        // ith index for s1 and upto jith index for s2 has been already evaluated
        // initialize a 2D vector of s1.size rows, s2.size columns with val -1
        vector<vector<int>> memo(s1.size(), vector<int>(s2.size(), -1));
        
        return rMemInterleave(s1, 0, s2, 0, s3, 0, memo);
    }
};
~~~

**Complexity Analysis**

Time complexity : O(2^{m+n}). m is the length of s1 and n is the length of s2.

Space complexity : O(m+n). The size of stack for recursive calls can go upto m+n.

### Approach 3: Using 2D Dynamic Programming

**Algorithm**

The recursive approach discussed in above solution included a character from one of the strings s1 or s2 in the resultant interleaved string and called a recursive function to check whether the remaining portions of s1 and s2 can be interleaved to form the remaining portion of s3. In the current approach, we look at the same problem the other way around. Here, we include one character from s1 or s2 and check whether the resultant string formed so far by one particular interleaving of the the current prefix of s1 and s2 form a prefix of s3.

Thus, this approach relies on the fact that the in order to determine whether a substring of s3(upto index kk), can be formed by interleaving strings s1 and s2 upto indices i and j respectively, solely depends on the characters of s1 and s2 upto indices i and j only and not on the characters coming afterwards.

To implement this method, we'll make use of a 2D boolean array dpdp. In this array dp[i][j]dp[i][j] implies if it is possible to obtain a substring of length (i+j+2) which is a prefix of s3 by some interleaving of prefixes of strings s1 and s2 having lengths (i+1) and (j+1) respectively. For filling in the entry of dp[i][j], we need to consider two cases:

1\. The character just included i.e. either at i^{th} index of s1s1 or at j^{th} index of s2 doesn't match the character at k^{th} index of s3, where k=i+j+1. In this case, the resultant string formed using some interleaving of prefixes of s1 and s2 can never result in a prefix of length k+1 in s3. Thus, we enter False at the character dp[i][j].

2\. The character just included i.e. either at i^{th} index of s1 or at j^{th} index of s2 matches the character at k^{th} index of s3, where k=i+j+1. Now, if the character just included(say x) which matches the character at k^{th} index of s3, is the character at i^{th} index of s1, we need to keep x at the last position in the resultant interleaved string formed so far. Thus, in order to use string s1s1 and s2 upto indices i and j to form a resultant string of length (i+j+2) which is a prefix of s3, we need to ensure that the strings s1 and s2 upto indices (i−1) and j respectively obey the same property.

Similarly, if we just included the j^{th} character of s2, which matches with the k^{th} character of s3, we need to ensure that the strings s1 and s2 upto indices i and (j−1) also obey the same property to enter a truetrue at dp[i][j].

This can be made clear with the following example:

~~~cpp
s1="aabcc"
s2="dbbca"
s3="aadbbcbcac"
~~~

Runtime: **12 ms**

Memory Usage: **8.7 MB**

**C++ Code**

~~~cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        // test edge case: s3 size doesn't equal sum of s1 and s2,
        // then s1 and s2 can't interleave to form s3
        if(s3.size() != s1.size() + s2.size()) {
            return false;
        }
        // create 2D vector containing s1.size vectors of size s2
        vector<vector<bool>> dp(s1.size()+1, vector<bool>(s2.size()+1));
        
        // perform 2D dynamic programming comparing s1 to s3 element
        // to see if they match, if false, comparing s2 to s3 element
        // to see if they match and storing bool in dp table
        // first dp[0][0] is set to T, then we see if there is a true
        // path that can be connected to last bool element in dp table
        // at dp[s1.size()][s2.size()] = dp[5][5], if true, return it
        for(int i = 0; i <= s1.size(); i++) {
            for(int j = 0; j <= s2.size(); j++) {
                // set dp[0][0] to true
                if(i == 0 && j == 0) {
                    dp[i][j] = true;
                }
                else if(i == 0) {
                    dp[i][j] = dp[i][j-1] && s2[j-1] == s3[i+j-1];
                }
                else if(j == 0) {
                    dp[i][j] = dp[i-1][j] && s1[i-1] == s3[i+j-1];
                }
                else {
                    dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) ||
                        (dp[i][j-1] && s2[j-1] == s3[i+j-1]);
                }
            }
        }
        // return last element in dp vector, if true, 
        // then s1 and s2 interleave to form s3
        return dp[s1.size()][s2.size()];
    }
};
~~~

**Complexity Analysis**

Time complexity: O(m⋅n). dp array of size m*n is filled.

Space complexity: O(m⋅n). 2D dp of size (m+1)*(n+1) is required. m and n are the lengths of strings s1 and s2 respectively.

### Approach 4: Using 1D Dynamic Programming

**Algorithm**

This approach is the same as the previous approach except that we have used only 1D dp array to store the results of the prefixes of the strings processed so far. Instead of maintaining a 2D array, we can maintain a 1D array only and update the array's element dp[i] when needed using dp[i-1] and the previous value of dp[i].

Runtime: **12 ms**

Memory Usage: **8.4 MB**

**C++ Code**

~~~cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        // test edge case: s3 size doesn't equal sum of s1 and s2,
        // then s1 and s2 can't interleave to form s3
        if(s3.size() != s1.size() + s2.size()) {
            return false;
        }
        // create 1D vector of length s2 
        vector<bool> dp(s2.size()+1);
        
        // perform 1D Dynamic Programming comparing s1 to s3 element
        // to see if they match, if false, comparing s2 to s3 element
        // to see if they match and storing bool in dp table
        // first dp[0] is set to T, then we see if there is a true
        // path that can be connected to last bool element in dp table
        // at dp[s2.size()] = dp[5], if true, return it
        for(int i = 0; i <= s1.size(); i++) {
            for(int j = 0; j <= s2.size(); j++) {
                // set dp[0][0] to true
                if(i == 0 && j == 0) {
                    dp[j] = true;
                }
                else if(i == 0) {
                    dp[j] = dp[j-1] && s2[j-1] == s3[i+j-1];
                }
                else if(j == 0) {
                    dp[j] = dp[j] && s1[i-1] == s3[i+j-1];
                }
                else {
                    dp[j] = (dp[j] && s1[i-1] == s3[i+j-1]) ||
                        (dp[j-1] && s2[j-1] == s3[i+j-1]);
                }
            }
        }
        // return last element in dp vector, if true, 
        // then s1 and s2 interleave to form s3
        return dp[s2.size()];
    }
};
~~~

**Complexity Analysis**

Time complexity: O(m⋅n). dp array of size n is filled m times.

Space complexity : O(n). n is the length of the string s1.
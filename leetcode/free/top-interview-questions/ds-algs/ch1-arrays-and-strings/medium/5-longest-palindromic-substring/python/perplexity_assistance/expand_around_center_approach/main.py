# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#25
#
##
# Before Coding
##
#
# Data Structure & Algorithm Concepts:
#
# - Palindrome Properties:
#   - A palindrome reads the same forward and backward
#   - Expanding around the center is a common technique to find palindromes efficiently
#
# - Dynamic Programming:
#   - Use a DP table to store whether a substring is a palindrome
#
# - Two Pointer Technique:
#   - Expand outward from a center (single or double) to find palindromes
#
# Clarifying Questions:
#
# 1. Are there multiple valid answers?
#   - Yes, return any one of the longest palindromic substrings if there are ties.
#
# 2. Can the input string be empty?
#   - No, constraints specify 1 <= s.length
#
# 3. Are all characters alphanumeric?
#   - Yes, the problem specifies English letters and digits
#
# Potential Solutions:
#
# 1. Brute Force:
#   - Check all substrings for palindromic properties (O(n^3))
#
# 2. Dynamic Programming:
#   - Use a DP table to store whether substrings are palindromes (O(n^2) time and space)
#
# 3. Expand Around Center:
#   - Treat each character (and gap between characters) as a potential center and expand
#       outward to find palindromes (O(n^2) time, O(1) space)
#
##
# After Coding
##
#
#   - Time Complexity: O(n^2)
#       - For each index i, we expand outward up to (n) times.
#       - Total Complexity O(n * n) = O(n^2)
#   - Space Complexity: O(1)
#       - No additional data structures are used; only variables are updated.
#   - Edge Cases:
#
# Potential Improvements:
#
# 1. Dynamic Programming Approach:
#   - Use a DP table (dp[i][j]) where True means substring s[i:j+1] is a palindrome
#   - Complexity: O(n^2) time and space
#
# 2. Manacher's Algorithm (Advanced):
#   - A linear-time algorithm specifically designed for finding the longest palindromic substring
#   - Complexity: O(n)
#
# Edge Cases:
#
# - Single character string (s = "a"): Return "a"
# - Entire string is a palindrome (s = "aaaa"): Return "aaaa".
# - No repeated characters (s = "abcde"): Return any single character
#

##
# While Coding
##
#
# Explanation of Expand Around Center Approach:
#
# 1. Helper Function (expand_around_center):
#   - Expands outward from two indices (left and right) as long as substring is a palindrome.
#
# 2 Iterate Over Centers:
#   - For each index i in the string:
#       - Treat i as the center for odd-length palindromes
#       - Treat i and i+1 as the center for even-length palindromes
#
# 3. Update Longest Palindrome:
#   - Compare the lengths of the current palindrome with longest
#   - Update longest if a longer palindrome is found
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            # Expand outward while the substring is a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindrome substring
            return s[left + 1:right]
        
        longest = ""

        for i in range(len(s)):
            # Odd-length palindromes (single character center)
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            
            # Even-length palindrome (two-character center)
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest

def main():
    sol = Solution()

    s1 = "babad"

    # Output: bab

    print(sol.longestPalindrome(s1))

if __name__ == "__main__":
    main()

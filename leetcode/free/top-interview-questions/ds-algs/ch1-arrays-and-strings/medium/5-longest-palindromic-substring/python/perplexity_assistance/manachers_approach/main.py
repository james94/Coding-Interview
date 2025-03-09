# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#26
#
##
# Before Coding
##
#
# Data Structure & Algorithm Concepts:
#

# Clarifying Questions:

# Potential Solutions:
#

##
# While Coding
##
#
# Implementation we'll use O(1) space
#
# Explanation of Solution:
#

##
# After Coding
##
#
#   - Time Complexity:
#   - Space Complexity:
#   - Edge Cases:

# Potential Improvements:
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

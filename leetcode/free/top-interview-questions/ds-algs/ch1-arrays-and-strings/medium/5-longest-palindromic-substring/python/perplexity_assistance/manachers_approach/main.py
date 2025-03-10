# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#26
#
##
# Before Coding
##
#
# Data Structure & Algorithm Concepts:
#
# - Palindrome Properties: Symmetric around a center, even/odd length handling
#
# - Manacher's Algorithm: Linear-time algorithm leveraging symmetry and dynamic
#   programming to avoid redundant checks
#
# Clarifying Questions:
#
# 1. Can there be multiple valid answers?
#   - Yes, but we need to return any one.
#
# 2. How to handle even-length palindromes?
#   - Transform the string to handle even/odd uniformly.
#
# 3. What if the string is empty?
#   - Constraints ensure s.length >= 1
#
# Potential Solutions:
#
# 1. Brute Force: Check all substrings O(n^3) time
#
# 2. Expand Around Center: O(n^2) time, O(1) space
#
# 3. Manacher's Algorithm: O(n) time, O(n) space
#
##
# After Coding
##
#
# - Time Complexity: O(n)
#   - Each character in the transformed string is processed once, and expansions are amortized O(n)
# - Space Complexity: O(n)
#   - Storing the transformed string and the P array
# - Edge Cases:
#   - Single Characters: Returns the character itself
#   - All Characters the Same: Returns the entire string
#   - No Palindrome: Returns the first character
#
# Potential Improvements:
#
# 1. Boundary Checks:
#   - Using sentinel characters (^ and $) avoids explicit boundary checks during expansion.
#
# 2. Parallelization:
#   - Not applicable here, but useful for distributed systems in related problems.
#


##
# While Coding
##
#
# Explanation of Manacher's Algorithm Approach:
#
# 1. String Transformation:
#
#   - Convert s to a new string with special characters (ex: "babad" -> ^#b#a#b#a#d#$). This
#       simplifies handling even/odd-length palindromes.
#
# 2. Palindrome Radius Array (P):
#   - P[i] stores the radius of the longest palindrome centered at index i in the transformed string.
#
# 3. Symmetry Optimization:
#   - Use the symmetry property to avoid redundant checks. If i is within the current
#       palindrome's right boundary (right), use the mirror index to initialize P[i]
#
# 4. Expansion:
#   - Expand around i as far as possible while maintaining the palindrome property.
#
# 5. Update Boundaries:
#   - If the current palindrome extends beyond right, update the center and right.
#
# 6. Track Maximum:
#   - Keep track of the longest palindrome found (max_len and max_center)
#
##
#   Summary
##
#
# This implementation of Manacher's Algorithm efficiently finds the longest palindromic substring
#   in linear time, leveraging symmetry and dynamic programming to minimize redundant checks.
#

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Transform the string with special characters
        transformed = '#'.join('^{}$'.format(s))
        n = len(transformed)
        P = [0] * n  # Longest palindrome radius array
        center = right = 0
        max_len = max_center = 0
        
        for i in range(1, n - 1):
            # Mirror index for the current center
            mirror = 2 * center - i
            
            # Initialize P[i] using symmetry if within the right boundary
            if i < right:
                P[i] = min(right - i, P[mirror])
            
            # Expand around the current center
            while transformed[i + P[i] + 1] == transformed[i - P[i] - 1]:
                P[i] += 1
            
            # Update center and right boundary if current palindrome expands past right
            if i + P[i] > right:
                center, right = i, i + P[i]
            
            # Track the maximum palindrome found
            if P[i] > max_len:
                max_len = P[i]
                max_center = i
        
        # Extract the longest palindrome from the original string
        start = (max_center - max_len) // 2
        end = start + max_len
        return s[start:end]

def main():
    sol = Solution()

    s1 = "babad"

    # Output: bab

    print(sol.longestPalindrome(s1))

if __name__ == "__main__":
    main()

# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#19

##
# Before Coding:
##
# Data Structures & Algorithms
#
# - Sliding Window Technique: Maintain a window of unique characters by adjusting start and end pointers
#
# - Hash Map/Dictionary: Track the most recent index of each character to optimize window adjustments
#
##
# Clarifying Questions:
##
#
# 1. Are the characters case-sensitive?
#   - Yes, the problem states "English letters", which include both cases
#
# 2. What constitutes a valid substring?
#   - A contiguous sequence of characters with no duplicates.
#
# Potential Solutions:
#
# 1. Brute Force: Check all possible substrings (O(n^3) time, impractical)
#
# 2. Sliding Window with Set: Track characters in a set, adjusting the window dynamically O(n) time
#
# 3. Optimized Sliding Window: Use a hash map to store the last seen index of each character, allowing immediate jumps (O(n) time)
#
##
# Explanation of Optimized Sliding Window Approach:
##
#
# 1. Initialization:
#   - char_index dictionary tracks the last occurrence of each character.
#   - start marks the beginning of the current window
#
# 2. Iterate with end pointer:
#   - If char is already in the window(char_index[char] >= start), move start to one position after its last occurrence
#   - Update char_index[char] to the current end
#   - Calculate the window length and update max_length
#
# 3. Result:
#   - Return max_length, which holds the length of the longest valid substring
#
##
# After Coding:
##
#
# Time Complexity: O(n), each character is processed exactly once
#
# Space Complexity: O(min(n, m)), where m is the size of the character set (ex: ASCII: 256, Unicode: larger). For practical purposes, this is O(1)
#
##
# Potential Improvements:
##
#
# 1. Array Instead of Hash Map:
#   - Use a fixed size array for ASCII characters (size 128 or 256) for faster lookups
#
# 2. Early Termination: 
#   - Exit early if the remaining characters cannot exceed the current max_length
#
##
# Edge Cases:
##

# We use Optimized Sliding Window: with Sliding Window and Hash Map/Dictionary
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {} # Stores the most recent index of each character
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            # If the character is in the map and within the current window, update start
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1

            # Update the character's latest index
            char_index[char] = end

            # Calculate current window length
            current_length = end - start + 1
            if current_length > max_length:
                max_length = current_length
        
        return max_length
    
def main():
    sol = Solution()

    s1 = "abcabcbb"

    print(sol.lengthOfLongestSubstring(s1))

    s2 = "bbbbb"

    print(sol.lengthOfLongestSubstring(s2))

    s3 = "pwwkew"

    print(sol.lengthOfLongestSubstring(s3))


if __name__ == "__main__":
    main()

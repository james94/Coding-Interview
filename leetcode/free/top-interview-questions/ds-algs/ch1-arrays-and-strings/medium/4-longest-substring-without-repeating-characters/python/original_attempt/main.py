
# Time Complexity: O(n), since we loop string
#
# Space Complexity: O(n), since we allocate memory for dictionary
#
# 15 mins, finished at 6 min 30 sec mark; Incorrect answer

# I think I had the right idea with dictionary, but needed to track longest substrings of string without duplicates

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr_dict = {}

        for i in range(len(s)):
            longest_substr_dict[s[i]] = i
        
        result_keys = list(longest_substr_dict.keys())
        # print(result_keys)
        result = len(result_keys)
        return result

def main():
    # s = "abcabcbb"
    s = "pwwkew"

    # Output: 3
    sol = Solution()
    
    print(sol.lengthOfLongestSubstring(s))
    # sol.lengthOfLongestSubstring(s)

if __name__ == "__main__":
    main()

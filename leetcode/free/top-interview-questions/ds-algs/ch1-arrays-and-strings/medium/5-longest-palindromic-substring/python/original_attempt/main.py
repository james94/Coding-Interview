class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        left = 0
        right = len(s) - 1
        result = ""

        while left < right:
            if s[left] == s[right]:
                result += s[left]
            else:
                right -= 1

def main():
    sol = Solution()
    s1 = "babad"

    # Output: bab

    print(sol.longestPalindrome(s1))
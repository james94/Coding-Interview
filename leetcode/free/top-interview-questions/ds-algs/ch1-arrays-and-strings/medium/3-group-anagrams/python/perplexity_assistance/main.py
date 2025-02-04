# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#1
# Able to type the solution in 3 mins

from typing import List
from collections import defaultdict

###
# Explanation:
###
#
# Hash Table: uses a dictionary where each key is a sorted string, and the 
#               corresponding value is a list of strings that are anagrams of each other
# Sorting: the characters in each string provides a consistent key for grouping anagrams
#
# Time Complexity: O(n*k*logk) where "n" is the number of strings and
    # "k" is the maximum length of a string. This is due to the sorting op
#
# Space Complexity: O(nk) for storing the dictionary and the output
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store groups of anagrams
        anagrams = {}

        # Iterate through each string in the input array
        for s in strs:
            # Sort the characters in the string to create a key
            sorted_s = "".join(sorted(s))

            # Use the sorted string as a key to store the original string in the dictionary
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                anagrams[sorted_s].append(s)

        # Return the values of the dictionary as the grouped anagrams
        return list(anagrams.values())

# Alternative Approach: Instead of sorting, we can do frequency count
    # of characters as the key, which would reduce the time complexity to O(nk)
    # by avoiding the sorting step
    def groupAnagramsV2(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            # Count the frequency of each character
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Use the frequency count as a key
            key = tuple(count)
            anagrams[key].append(s)
        
        return list(anagrams.values())

def main():
    soln = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    # result = soln.groupAnagrams(strs)
    result = soln.groupAnagramsV2(strs)
    print(f"{result}")

if __name__ == "__main__":
    main()

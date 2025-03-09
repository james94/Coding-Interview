
import heapq
from collections import Counter


# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-Je6PtfnLTsu.hvXrYVTNzQ#1

####
#   Data Structures & Algorithm Concepts
####
#
#   Potential Algorithms/Solutions:
#
#   Hash Map and Sorting: Count frequencies using a hash map and then sort the map
#       entries by frequency
#
#   Hash Map and Heap: Use a hash map to count frequencies and a heap to efficiently
#       retrieve the top k elements
#
#   Bucket Sort: use this sort where each bucket represents a frequency count
#
####
#   Clarifying Questions
####
#
#   Are there any constraints on the input size or the range of values?
#
#   Can we use extra space? Problem doesn't explicitly restrict extra space, but
#       efficiency is implied
#
####
#   Big O Notation
####
#
#   Time Complexity: Hash Map and Heap solution is O(n * logk), which is better than O(n * logn)
#
#   Space Complexity: O(n) space for the hash map and O(k) space for the heap, which is efficient
#


# We'll use Hash Map Counter and Heap as it efficiently meets the time complexity requirement
def topKFrequent(nums, k):
    # Count the frequency of each element
    count = Counter(nums)

    # USe a heap to find the top k frequent elements
    return heapq.nlargest(k, count.keys(), key=count.get)

def main():
    nums = [1,1,1,2,2,3] 
    k = 2

    res = topKFrequent(nums, k)
    print(res)

if __name__ == "__main__":
    main()
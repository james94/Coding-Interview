# Longest Scoring Streak (Solution)

## Before Coding

### Clarifying questions:

1. Are the scores to be non-negative integers?

2. Should we consider scores equal to the threshold as part of the streak?

3. What should we return if there's no streak above the threshold?

4. Is there a maximum limit for the array length or score?

### Potential solutions:

1. Linear scan with a sliding window approach.

2. Two-pointer technique

3. Dynamic programming

## Implementation

We'll implement the solution using a linear scan approach:

- [main.py](./python/main.py)

## While Coding

### 1. **Data Structures and Algorithms**:

- Use a simple array traversal
- No additional data structures needed, making it memory efficient

### 2. **Big-O Notation**:

- Time Complexity: O(n), where n is the number of scores
- Space Complexity: O(1), as we only use two variables regardless of input size

## After Coding

### Potential Improvements

1. We could modify the function to return the start and end indices of the longest streak.

2. For real-time updates, we could implement a sliding window approach that efficiently
updates the streak as new scores are added.

3. We could add error handling for invalid inputs (ex: negative scores or thresholds).

## Follow-Up: Question Answers

1. How would you modify your solution if you needed to find multiple streaks above the threshold,
returning their start and end indices?

- To find multiple streaks with start and end indices, we could modify the function to
return a list of tuples (start, end) for each streak above the threshold.

2. Can you optimize your solution to handle real-time updates, where new scores are
constantly being added?

- For real-time updates, we could use a sliding window approach or maintain a data structure
like a deque to efficiently update the streak as new scores are added.

3. How would you adapt your algorithm if you needed to find the longest streak where
the average score is above the threshold, rather than each individual score?

- To find the longest streak where the average score is above the threshold, we would
need to maintain a running sum and count of scores in the current streak, calculating
the average at each step.

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-FjkdnjniRhykBYk.gzlreQ

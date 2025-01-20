# Longest Scoring Streak

## Problem Statement

Given an array of integers representing a player's game-by-game scoring and a threshold value,
implement a function to find the longest streak of consecutive games where the player scored 
above the given threshold.

## Examples

### Example 1

**Input:**

~~~python
scores = [30, 25, 40, 32, 18, 20, 22, 28, 30, 35]

threshold = 25
~~~

**Output:**

~~~python
4
~~~

**Explanation:**

The longest streak of scores above 25 is `[30, 25, 40, 32]`.
Although 25 equals the threshold, we consider it as part of the streak.

### Example 2

**Input:**

~~~python
scores = [10, 15, 20, 25, 30, 35, 40]

threshold = 22
~~~

**Output:**

~~~python
5
~~~

**Explanation:**

The longest streak of scores above 22 is `[25, 30, 35, 40]`.

### Example 3

**Input:**

~~~python
scores = [50, 45, 40, 35, 30]

threshold = 55
~~~

**Output:**

~~~python
0
~~~

**Explanation:**

No scores are above the threshold, so the longest streak is 0.

### Example 4

**Input:**

~~~python
scores = [22, 23, 24, 25, 26, 27, 28, 29, 30]

threshold = 25
~~~

**Output:**

~~~python
6
~~~

**Explanation:**

The longest streak of scores above or equal to 25 is `[25, 26, 27, 28, 29, 30]`.

## Constraints

~~~python
1 <= scores.length <= 10^5

0 <= scores[i] <= 100

0 <= threshold <= 100
~~~

## Follow-Up

1. How would you modify your solution if you needed to find multiple streaks above the threshold,
returning their start and end indices?

2. Can you optimize your solution to handle real-time updates, where new scores are
constantly being added?

3. How would you adapt your algorithm if you needed to find the longest streak where
the average score is above the threshold, rather than each individual score?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A

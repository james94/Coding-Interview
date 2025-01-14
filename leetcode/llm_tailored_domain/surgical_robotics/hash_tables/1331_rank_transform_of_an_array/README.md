# 1331. Rank Transform of an Array (Surgical Robotics)

Leetcode Reference Original Problem: 

Perplexity AI updated wording of leetcode question tailoring for surgical robotics: https://www.perplexity.ai/search/you-are-a-software-infrastruct-XzSlP3FyT9Ohg9goUONhCQ

## Overview

### Surgical Robot Precision Ranking System

You are developing a software system for a surgical robot that performs minimally invasive procedures. The robot's arm movements are controlled by an array of sensor readings, where each reading represents the precision of a particular movement in micrometers. Your task is to implement a ranking system for these movements to help surgeons evaluate and improve the robot's performance.

Design and implement a function that takes an array of movement precision readings and replaces each reading with its rank. The ranking system should follow these rules:

1. Ranks start from 1.

2. More precise movements (smaller values) receive lower ranks.

3. If two movements have the same precision, they should have the same rank.

4. Ranks should be as small as possible while maintaining the above rules.

Your implement should be optimized for both time and space complexity, considering that the system may need to process large datasets in real-time during surgeries.

## Example 1

~~~bash
Input: precisionReadings = [40, 10, 20, 30] (micrometers)
Output: [4, 1, 2, 3]
Explanation: 10 is the most precise (rank 1), followed by 20, 30, and 40.
~~~

## Example 2

~~~bash
Input: precisionReadings = [5, 5, 5] (micrometers)
Output: [1, 1, 1]
Explanation: All movements have the same precision, so they share rank 1.
~~~

## Example 3

~~~bash
Input: precisionReadings = [37, 12, 28, 9, 100, 56, 80, 5, 12] (micrometers)
Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]
~~~


## Constraints:

- 0 <= precisionReadings.length <= 10^5
- 1 <= precisionReadings[i] <= 10^9 (all readings are positive integers representing micrometers)

## Additional Requirements

1. Discuss the time and space complexity of your soltuion.

2. Explain how you would handle potential concurrency issues if this system were to be used in a multi-threaded environment during surgery.

3. Describe how you would modify your solution to handle real-time streaming data from the robot's sensors.

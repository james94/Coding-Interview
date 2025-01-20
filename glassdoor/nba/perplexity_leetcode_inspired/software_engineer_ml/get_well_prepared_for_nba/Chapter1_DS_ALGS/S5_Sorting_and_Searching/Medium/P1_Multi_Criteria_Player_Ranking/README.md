# Multi-Criteria Player Ranking Algorithm

## Problem Statement

Implement a sorting algorithm to rank NBA players based on multiple statistical categories.
The algorithm should take into account various performance metrics and produce a sorted
list of players from best to worst.

## Examples

### Example 1

**Input:**

~~~yml
Players: [("LeBron James", 27.4, 8.3, 8.1), ("Nikola Jokic", 26.2, 10.5, 8.3), ("Giannis Antetokounmpo", 29.9, 11.6, 5.8)]

Categories: [Points, Rebounds, Assists]

Weights: [0.5, 0.3, 0.2]
~~~

**Output:**

~~~yml
Output: ["Giannis Antetokounmpo", "Nikola Jokic", "LeBron James"]
~~~

**Explanation:**

Giannis ranks highest due to his strong performance in points and rebounds, which have higher weights.

### Example 2

**Input:**

~~~yml
Players: [("Stephen Curry", 25.5, 5.2, 6.3, 42.7), ("Luka Doncic", 28.4, 9.1, 8.7, 35.4), ("Jayson Tatum", 26.9, 8.0, 4.4, 37.6)]

Categories: [Points, Rebounds, Assists, 3P%]

Weights: [0.3, 0.2, 0.2, 0.3]
~~~

**Output:**

~~~yml
Output: ["Stephen Curry", "Luka Doncic", "Jayson Tatum"]
~~~

**Explanation:**

Curry's high 3P% compensates for lower rebounds and assists, giving him the top rank.


### Example 3

**Input:**

~~~yml
Players: [("Joel Embiid", 30.6, 11.7, 4.2, 1.8), ("Anthony Davis", 25.9, 12.5, 2.6, 2.0), ("Rudy Gobert", 14.4, 12.7, 1.2, 2.3)]

Categories: [Points, Rebounds, Assists, Blocks]

Weights: [0.4, 0.3, 0.1, 0.2]
~~~

**Output:**

~~~yml
Output: ["Joel Embiid", "Anthony Davis", "Rudy Gobert"]
~~~

**Explanation:**

Embiid's superior scoring outweighs Davis's slight advantages in rebounds and blocks.

## Constraints


- 2 <= Number of players <= 500
- 2 <= Number of statistical categories <= 10
- 0 <= Stat values <= 100
- 0 < Weight values <= 1
- Sum of weights equals 1

## Follow-Up

1. How would you modify your algorithm to handle ties between players?

2. Can you implement a feature to allow for dynamic weighting of categories based on user input?

3. How would you adapt your solution to handle advanced statistics like Player
Efficiency Rating (PER) or True Shooting Percentage (TS%)?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
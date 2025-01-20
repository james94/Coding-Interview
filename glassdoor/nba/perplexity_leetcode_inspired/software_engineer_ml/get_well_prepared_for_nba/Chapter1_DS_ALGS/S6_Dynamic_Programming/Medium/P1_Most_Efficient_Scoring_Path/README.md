# Most Efficient Scoring Path

## Problem Statement

Design a dynamic programming algorithm to calculate the most efficient path for a player
to score, considering defender positions on a basketball court. The court is represented
as a grid where each cell can be empty, occupied by a defender, or contain the player or
the basket. The player can move in four directions: up, down, left, or right. The
efficiency of a path is determined by the number of moves and the proximity to defenders.

## Examples

### Example 1

**Input:**

~~~yml
Court size: 5x5

Player position: (0, 0)

Basket position: (4, 4)

Defenders: [(1, 1), (2, 2), (3, 3)]
~~~

**Output:**

~~~yml
Output: [(0, 0), (0, 1), (1, 2), (2, 3), (3, 4), (4, 4)]
~~~

**Explanation:**

The path avoids defenders diagonally while minimizing the number of moves.

### Example 2

**Input:**

~~~yml
Court size: 4x4

Player position: (0, 0)

Basket position: (3, 3)

Defenders: [(1, 1), (2, 2)]
~~~

**Output:**

~~~yml
Output: [(0, 0), (0, 1), (0, 2), (1, 3), (2, 3), (3, 3)]
~~~

**Explanation:**

The path goes around the defenders by moving right and then up.


### Example 3

**Input:**

~~~yml
Court size: 6x6

Player position: (0, 3)

Basket position: (5, 3)

Defenders: [(2, 2), (2, 3), (2, 4), (3, 3)]
~~~

**Output:**

~~~yml
Output: [(0, 3), (1, 2), (2, 1), (3, 2), (4, 3), (5, 3)]
~~~

**Explanation:**

The path navigates around the cluster of defenders.

## Constraints


- 3 <= Court size <= 20
- Player and basket positions are within the court boundaries
- 0 <= Number of defenders < (Court size)^2 - 2
- Player and basket positions will not be occupied by defenders
- There will always be at least one valid path to the basket

## Follow-Up

1. How would you modify your algorithm to account for different levels of defensive
pressure in each cell?

2. Can you adapt your solution to handle moving defenders?

3. How would you extend your algorithm to consider the player's shooting range and incorporate the option
to take a shot from a distance?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
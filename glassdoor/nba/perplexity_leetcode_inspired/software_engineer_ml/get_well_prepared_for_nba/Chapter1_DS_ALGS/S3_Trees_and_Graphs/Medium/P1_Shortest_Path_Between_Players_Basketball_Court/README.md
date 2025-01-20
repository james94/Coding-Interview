# Shortest Path Between Players on Basketball Court

## Problem Statement

Develop an algorithm to find the shortest path between two players on a basketball court,
considering obstacles such as other players or court equipment. The court is represented
as a 2D grid where each cell can be empty, occupied by a player, or contain an obstacle.
The algorithm should return the shortest path avoiding all obstacles.

## Examples

### Example 1

**Input:**

~~~yml
Court size: 10x10

Start player position: (0, 0)

End player position: (9, 9)

Obstacles: [(2, 2), (3, 3), (4, 4), (5, 5)]
~~~

**Output:**

~~~yml
Output: [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (9, 9)]
~~~

**Explanation:**

The path avoids the diagonal line of obstacles by moving around them.

### Example 2

**Input:**

~~~yml
Court size: 5x5

Start player position: (0, 0)

End player position: (4, 4)

Obstacles: [(1, 1), (2, 2), (3, 3)]
~~~

**Output:**

~~~yml
Output: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 4)]
~~~

**Explanation:**

The path goes around the obstacles by moving right and then up.


### Example 3

**Input:**

~~~yml
Court size: 7x7

Start player position: (0, 3)

End player position: (6, 3)

Obstacles: [(2, 2), (2, 3), (2, 4), (4, 2), (4, 3), (4, 4)]
~~~

**Output:**

~~~yml
Output: [(0, 3), (1, 3), (1, 4), (2, 5), (3, 5), (4, 5), (5, 4), (5, 3), (6, 3)]
~~~

**Explanation:**

The path navigates through two "walls" of obstacles.

## Constraints


- 5 <= Court size <= 50
- 0 <= Start/End player positions < Court size
- 0 <= Number of obstacles < (Court size)^2
- Start and end positions will not be obstacles
- There will always be a valid path between the start and end positions


## Follow-Up

1. How would you modify your algorithm to handle moving obstacles (ex: other players)?

2. Can you optimize your algorithm to work efficiently on larger court sizes?

3. How would you adapt your solution to find the shortest path for a player to intercept a moving ball?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
# Most Central Player in Passing Network

## Problem Statement (Graphs)

Design a graph representation of player passing networks and implement a function to find
the most central player. The centrality of a player is determined by their eigenvector
centrality, which measures their importance in the network based on the number and
quality of their connections.

## Examples

### Example 1

**Input:**

~~~yml
Passes: [("Player1", "Player2", 5), ("Player2", "Player3", 3), ("Player3", "Player1", 2), ("Player1", "Player3", 4)]
~~~

**Output:**

~~~yml
Output: "Player1"
~~~

**Explanation:**

Player1 has the highest eigenvector centrality due to more frequent and diverse passing connections.

### Example 2

**Input:**

~~~yml
Passes: [("PlayerA", "PlayerB", 2), ("PlayerB", "PlayerC", 2), ("PlayerC", "PlayerD", 2), ("PlayerD", "PlayerA", 2)]
~~~

**Output:**

~~~yml
Output: Any player (all have equal centrality)
~~~

**Explanation:**

In this circular passing pattern, all players have equal eigenvector centrality.

### Example 3

**Input:**

~~~yml
Passes: [("Star", "Player1", 10), ("Star", "Player2", 8), ("Star", "Player3", 9), ("Player1", "Player2", 1), ("Player2", "Player3", 1)]
~~~

**Output:**

~~~yml
Output: "Star"
~~~

**Explanation:**

The "Star" player has significantly more passes and connections, resulting in
the highest eigenvector centrality.

## Constraints

- 2 <= Number of players <= 15
- 1 <= Number of passes <= 1000
- 1 <= Pass weight <= 100
- Player names are unique strings

## Follow-Up

1. How would you modify your algorithm to account for the quality of passes 
(ex: passes leading to assists or shots)?

2. Can you implement a function to identify potential weak links in the passing network?

3. How would you adapt your solution to analyze passing networks across multiple
games and identify consistent patterns?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A

# Generate All Possible Lineups

## Problem Statement

Implement a recursive algorithm to generate all possible lineups given a set of NBA
players. A valid lineup consists of 5 players with positions: Point Guard (PG),
Shooting Guard (SG), Small Forward (SF), Power Forward (PF), and Center (C).
Each player can only be used once in a lineup.

## Examples

### Example 1

**Input:**

~~~yml
Players: [("Curry", "PG"), ("Thompson", "SG"), ("Wiggins", "SF"), ("Green", "PF"), ("Looney", "C")]
~~~

**Output:**

~~~yml
Output: [["Curry", "Thompson", "Wiggins", "Green", "Looney"]]
~~~

**Explanation:**

Only one valid lineup can be formed with the given players.

### Example 2

**Input:**

~~~yml
Players: [("Curry", "PG"), ("Paul", "PG"), ("Thompson", "SG"), ("Wiggins", "SF"), ("Green", "PF"), ("Looney", "C")]
~~~

**Output:**

~~~yml
Output: [
["Curry", "Thompson", "Wiggins", "Green", "Looney"],
["Paul", "Thompson", "Wiggins", "Green", "Looney"]
]
~~~

**Explanation:**

Two valid lineups can be formed. The PG position can be filled by either Curry or Paul.


### Example 3

**Input:**

~~~yml
Players: [("Curry", "PG"), ("Paul", "PG"), ("Thompson", "SG"), ("Poole", "SG"), ("Wiggins", "SF"), ("Green", "PF"), ("Looney", "C")]
~~~

**Output:**

~~~yml
Output: [
["Curry", "Thompson", "Wiggins", "Green", "Looney"],
["Curry", "Poole", "Wiggins", "Green", "Looney"],
["Paul", "Thompson", "Wiggins", "Green", "Looney"],
["Paul", "Poole", "Wiggins", "Green", "Looney"]
]
~~~

**Explanation:**

Four valid lineups can be formed by combining different PG and SG options.

## Constraints


- 5 <= Number of players <= 15
- Each player has a valid position (PG, SG, SF, PF, or C)
- There is at least one player for each position
- Player names are unique strings

## Follow-Up

1. How would you modify your algorithm to generate lineups that meet a salary cap constraint?

2. Can you optimize your solution to handle larger sets of players efficiently?

3. How would you adapt your algorithm to generate lineups with different position
requirements (ex: 2 guards, 2 forwards, 1 center)?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
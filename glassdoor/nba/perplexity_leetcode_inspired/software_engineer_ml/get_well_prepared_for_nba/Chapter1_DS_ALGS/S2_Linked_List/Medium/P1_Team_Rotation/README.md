# Team Rotation Linked List

## Problem Statement

Implement a linked list data structure to represent a basketball team's rotation during a
game. The linked list should allow for efficient player substitutions, including adding
players to the rotation, removing players, and moving players to different positions in the
rotation. Each node in the linked list should represent a player and contain their name
and position.

## Examples

### Example 1

**Input:**

~~~yml
Add players: ["LeBron James", "Anthony Davis", "Russell Westbrook", "Carmelo Anthony", "Dwight Howard"]

Substitute: Remove "Dwight Howard", Add "Malik Monk" at position 3
~~~

**Output:**

~~~yml
Output: LeBron James -> Anthony Davis -> Malik Monk -> Russell Westbrook -> Carmelo Anthony
~~~

**Explanation:**

The initial rotation is created, then Dwight Howard is removed and Malik Monk is inserted at position 3.

### Example 2

**Input:**

~~~yml
Add players: ["Stephen Curry", "Klay Thompson", "Draymond Green"]

Substitute: Move "Draymond Green" to position 1
~~~

**Output:**

~~~yml
Output: Draymond Green -> Stephen Curry -> Klay Thompson
~~~

**Explanation:**

The initial rotation is created, then Draymond Green is moved to the front of the rotation.


### Example 3

**Input:**

~~~yml
Add players: ["Kevin Durant", "Kyrie Irving"]

Substitute: Add "James Harden" at position 3, Remove "Kyrie Irving"
~~~

**Output:**

~~~yml
Output: Kevin Durant -> James Harden
~~~

**Explanation:**

The initial rotation is created with two players, James Harden is added at the end, and then Kyrie Irving is removed.

## Constraints


- 1 <= Number of players in rotation <= 15

- Player names are unique strings

- Position values are 1-indexed


## Follow-Up

1. How would you modify your implementation to handle a maximum rotation size (ex: 5 players on the court at a time)?

2. Can you implement a function to swap the positions of two players in the rotation efficiently?

3. How would you extend your linked list to store additional player statistics (ex: minutes played, points scored)
and update them during the game?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A

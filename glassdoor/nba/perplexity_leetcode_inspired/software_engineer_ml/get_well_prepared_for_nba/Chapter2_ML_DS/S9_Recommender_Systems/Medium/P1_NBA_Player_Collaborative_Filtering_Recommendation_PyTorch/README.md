# NBA Player Recommender System: Collaborative Filtering with PyTorch

## Problem Statement

Implement a collaborative filtering recommender system using PyTorch to suggest similar
NBA players based on their performance metrics. The system should learn player
embeddings from historical performance data and use these to recommend players with
similar playing styles or abilities.

## Examples

### Example 1

**Input:**

~~~yml
Player: LeBron James
Performance Metrics: [Points: 27.4, Rebounds: 8.3, Assists: 8.1, Steals: 1.2, Blocks: 0.8]
~~~

**Output:**

~~~yml
Similar Players: [Luka Doncic, Giannis Antetokounmpo, Nikola Jokic]
~~~

**Explanation:**

The model suggests players with versatile skill sets similar to LeBron James.

### Example 2

**Input:**

~~~yml
Player: Stephen Curry
Performance Metrics: [Points: 29.5, 3PT%: 42.7, Assists: 6.3, Steals: 1.4]
~~~

**Output:**

~~~yml
Similar Players: [Damian Lillard, Trae Young, Devin Booker]
~~~

**Explanation:**

The system recommends players known for their shooting and scoring abilities.

### Example 3

**Input:**

~~~yml
Player: Rudy Gobert
Performance Metrics: [Rebounds: 12.7, Blocks: 2.3, FG%: 67.5]
~~~

**Output:**

~~~yml
Similar Players: [Clint Capela, Jarrett Allen, Mitchell Robinson]
~~~

**Explanation:**

The model suggests players with strong defensive and rebounding skills.


## Constraints


- Number of Players: 300-500
- Embedding Dimension: 32-128
- Performance Metrics: 5-10 key statistics per player
- Training Data: Last 3-5 seasons of player performance
- Similarity Measure: Cosine similarity between player embeddings

## Follow-Up

1. How would you handle new players with limited performance data?

2. Can you modify the model to incorporate team performance or player synergies?

3. What techniques would you use to explain the recommendations to users?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
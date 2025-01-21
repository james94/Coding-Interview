# NBA Game Summary Generation from Play-by-Play Data

## Problem Statement

Implement a transformer-based model using PyTorch to generate concise game summaries from 
NBA play-by-play data. The model should take in a sequence of play-by-play events and produce 
a coherent summary highlighting key moments and statistics of the game.


## Examples

### Example 1

**Input:**

~~~yml
Play-by-play sequence: ["Q1 12:00 - Jump ball won by Team A", 
"Q1 11:45 - Player X (Team A) makes 3-pt jump shot", 
"Q1 11:20 - Player Y (Team B) misses layup", ...]
~~~

**Output:**

~~~yml
Summary: "Team A secured an early lead with a strong start from Player X, 
who opened the scoring with a 3-pointer. Despite Team B's efforts, Team A 
maintained control throughout, winning 105-98. Player X finished with a game-high 28 points."
~~~

**Explanation:**

The model extracts key events and statistics to create a concise summary of the game flow and outcome.


### Example 2

**Input:**

~~~yml
Play-by-play sequence: ["Q4 0:45 - Player Z (Team B) makes game-tying 3-pt shot", 
"Q4 0:10 - Player W (Team A) misses potential game-winner", 
"OT1 4:55 - Team B wins jump ball", ...]
~~~

**Output:**

~~~yml
Summary: "In a thrilling finish, Team B forced overtime with a clutch 3-pointer by Player Z. 
The extra period saw Team B dominate, outscoring Team A 15-7 to secure a 112-104 victory. 
Player Z led all scorers with 32 points."
~~~

**Explanation:**

The model identifies the dramatic late-game events and highlights the key performances in overtime.

## Constraints


- Input: Sequence of play-by-play events (50-200 events per game)
- Output: Summary text (50-100 words)
- Model Architecture: Transformer-based encoder-decoder
- Tokenizer: BERT tokenizer (vocab size: 30522)
- Training Data: 1000-5000 NBA games with play-by-play data and human-written summaries

## Follow-Up

1. How would you handle the varying length of play-by-play sequences for different games?

2. Can you modify the model to generate summaries focusing on specific players or game aspects?

3. What techniques would you use to ensure the generated summaries are factually accurate?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
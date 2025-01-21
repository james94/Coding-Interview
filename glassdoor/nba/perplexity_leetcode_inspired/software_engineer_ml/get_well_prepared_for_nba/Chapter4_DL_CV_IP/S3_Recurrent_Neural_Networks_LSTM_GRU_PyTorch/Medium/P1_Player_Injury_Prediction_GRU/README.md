# Player Injury Prediction using GRU

## Problem Statement

Design a Gated Recurrent Unit (GRU) based model using PyTorch to analyze time-series data 
of player movements and predict potential injuries. The model should take in sequences of 
player movement data and output the probability of injury occurrence.

## Examples

### Example 1

**Input:**

~~~yml
Sequence of movement data: [[acceleration: 2.3 m/s², speed: 4.5 m/s, change of direction: 15°], ...]
Sequence length: 100 time steps
~~~

**Output:**

~~~yml
Injury probability: 0.75
~~~

**Explanation:**

High acceleration and frequent direction changes over the sequence indicate a higher risk of injury.


### Example 2

**Input:**

~~~yml
Sequence of movement data: [[acceleration: 1.5 m/s², speed: 3.2 m/s, change of direction: 5°], ...]
Sequence length: 100 time steps
~~~

**Output:**

~~~yml
Injury probability: 0.15
~~~

**Explanation:**

Lower intensity movements suggest a lower risk of injury.

### Example 3

**Input:**

~~~yml
Sequence of movement data: [[acceleration: 3.1 m/s², speed: 5.5 m/s, change of direction: 25°], ...]
Sequence length: 100 time steps
~~~

**Output:**

~~~yml
Injury probability: 0.92
~~~

**Explanation:**

Very high intensity movements with sharp direction changes indicate a high risk of injury.


## Constraints


- Input features: 3-5 movement metrics
- Sequence length: 50-200 time steps
- GRU layers: 1-3
- Hidden size: 32-128
- Output: Binary classification (0 for no injury risk, 1 for injury risk)

## Follow-Up

1. How would you modify the model to handle variable-length input sequences?

2. Can you extend the model to predict specific types of injuries (e.g., ankle sprain, ACL tear)?

3. What techniques would you use to interpret which movement patterns contribute most to injury risk?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
# NBA All-Star Selection Multimodal Network

## Problem Statement

Implement a multimodal neural network using PyTorch that combines player statistics and image data 
to predict NBA All-Star selections. The model should process both numerical performance metrics and 
player images to make predictions.

## Examples

### Example 1

**Input:**

~~~yml
Player Stats: [Points: 28.5, Rebounds: 8.3, Assists: 7.2, PER: 25.1]
Player Image: 64x64 RGB image of the player in action
~~~

**Output:**

~~~yml
All-Star Probability: 0.92
~~~

**Explanation:**

High statistical performance combined with visual cues from the image indicate a likely All-Star selection.


### Example 2

**Input:**

~~~yml
Player Stats: [Points: 18.7, Rebounds: 5.5, Assists: 4.2, PER: 17.8]
Player Image: 64x64 RGB image of the player in action
~~~

**Output:**

~~~yml
All-Star Probability: 0.35
~~~

**Explanation:**

Average statistics and less distinctive visual features suggest a lower probability of All-Star selection.

### Example 3

**Input:**

~~~yml
Player Stats: [Points: 22.3, Rebounds: 11.5, Assists: 2.8, PER: 21.5]
Player Image: 64x64 RGB image of the player in action
~~~

**Output:**

~~~yml
All-Star Probability: 0.78
~~~

**Explanation:**

Strong rebounding numbers and visual indicators of physicality contribute to a higher All-Star probability.


## Constraints


- Input Features: 4-6 player statistics
- Image Size: 64x64 RGB
- CNN Architecture: Pre-trained ResNet18
- Output: Binary classification (0 for non-All-Star, 1 for All-Star)
- Training Data Size: 1000-5000 player seasons

## Follow-Up

1. How would you handle class imbalance given that All-Stars are a small percentage of all players?

2. Can you modify the model to provide interpretability for its predictions?

3. What techniques would you use to prevent overfitting, especially with the image data?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
# NBA Player Position Prediction: Decision Tree Classifier

## Problem Statement

Implement a decision tree classifier to predict an NBA player's position based on their
physical attributes and performance statistics, considering the evolving naature of
player roles in modern basketball.

## Examples

### Example 1

**Input:**

~~~yml
Physical Attributes: [Height: 6.8, Weight: 220, Wingspan: 7.2]

Performance Stats: [Points: 22.5, Rebounds: 7.2, Assists: 5.8, Blocks: 1.5]
~~~

**Output:**

~~~yml
Output: Power Forward
~~~

**Explanation:**

Combination of physical size and versatile statistical profile suggests a power forward role

### Example 2

**Input:**

~~~yml
Physical Attributes: [Height: 6.3, Weight: 190, Wingspan: 6.8]

Performance Stats: [Points: 18.7, Rebounds: 3.5, Assists: 6.3, Blocks: 0.2]
~~~

**Output:**

~~~yml
Output: Point Guard
~~~

**Explanation:**

Smaller frame with high assist numbers indicates a point guard position

### Example 3

**Input:**

~~~yml
Physical Attributes: [Height: 7.0, Weight: 250, Wingspan: 7.5]

Performance Stats: [Points: 12.3, Rebounds: 10.5, Assists: 1.2, Blocks: 2.3]
~~~

**Output:**

~~~yml
Output: Center
~~~

**Explanation:**

Tall stature with high rebounding and blocking stats suggests a center role


## Constraints


- Input Features: 7-10 physical and performance metrics
- Training Data Size: 200-500 player records
- Position Classification: 5 positions (PG, SG, SF, PF, C)
- Model Complexity: Multi-layer neural network simulating decision tree behavior

## Follow-Up

1. How would you handle the increasing "positionless" nature of modern NBA basketball?

2. Can you modify the model to provide position probability distributions?

3. What techniques would you use to improve model generalization?

The implementation draws insights from the search results, particularly the research showing that:

- SVM and Random Forest models achieve around 74% accuracy in player position classification
- Physical attributes and performance statistics are crucial for position prediction
- Modern NBA positions are becoming increasingly fluid and hybridized

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
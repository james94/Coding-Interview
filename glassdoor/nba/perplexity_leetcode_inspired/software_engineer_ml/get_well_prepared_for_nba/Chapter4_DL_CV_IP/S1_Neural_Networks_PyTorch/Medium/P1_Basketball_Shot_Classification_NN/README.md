# Basketball Shot Classification Neural Network

## Problem Statement

Implement a basic neural network using PyTorch to classify basketball shots as made or missed 
based on trajectory data. The model should take in features extracted from the shot trajectory 
and output a binary classification.

## Examples

### Example 1

**Input:**

~~~yml
Trajectory Features: [Release Angle: 52°, Initial Velocity: 7.2 m/s, Release Height: 2.1 m, Distance to Basket: 6.7 m]
~~~

**Output:**

~~~yml
Classification: Made (0.92 probability)
~~~

**Explanation:**

The combination of a high release angle and appropriate velocity suggests a successful shot.


### Example 2

**Input:**

~~~yml
Trajectory Features: [Release Angle: 40°, Initial Velocity: 6.5 m/s, Release Height: 2.0 m, Distance to Basket: 7.5 m]
~~~

**Output:**

~~~yml
Classification: Missed (0.78 probability)
~~~

**Explanation:**

The lower release angle and velocity for the given distance indicate a likely miss.

### Example 3

**Input:**

~~~yml
Trajectory Features: [Release Angle: 48°, Initial Velocity: 7.8 m/s, Release Height: 2.3 m, Distance to Basket: 5.5 m]
~~~

**Output:**

~~~yml
Classification: Made (0.85 probability)
~~~

**Explanation:**

The higher initial velocity compensates for the shorter distance, suggesting a successful shot.


## Constraints


- Input Features: 4-6 trajectory parameters
- Output: Binary classification (0 for miss, 1 for made)
- Hidden Layers: 2-3 layers
- Activation Functions: ReLU for hidden layers, Sigmoid for output
- Training Data Size: 1000-5000 shot trajectories

## Follow-Up

1. How would you handle imbalanced datasets where made shots are less frequent than misses?

2. Can you modify the model to provide shot accuracy percentage instead of binary classification?

3. What techniques would you use to visualize the decision boundary of your neural network?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
# Basketball Play Classification CNN

## Problem Statement

Implement a Convolutional Neural Network (CNN) using PyTorch to classify different types of 
basketball plays from court diagrams. The model should take as input an image of a basketball 
play diagram and output the predicted play type.

## Examples

### Example 1

**Input:**

~~~yml
Input: Image of a pick and roll play diagram
~~~

**Output:**

~~~yml
Output: "Pick and Roll" (0.92 probability)
~~~

**Explanation:**

The CNN correctly identifies the characteristic movement patterns of a pick and roll play from the diagram.


### Example 2

**Input:**

~~~yml
Input: Image of an isolation play diagram
~~~

**Output:**

~~~yml
Output: "Isolation" (0.88 probability)
~~~

**Explanation:**

The model recognizes the spacing and positioning typical of an isolation play.

### Example 3

**Input:**

~~~yml
Input: Image of a motion offense play diagram
~~~

**Output:**

~~~yml
Output: "Motion Offense" (0.75 probability)
~~~

**Explanation:**

The CNN identifies the multiple player movements and passing options characteristic of a motion offense.


## Constraints


- Input: RGB images of basketball play diagrams
- Image Size: 64x64 pixels (after resizing)
- Number of Play Types: 5-10 different plays
- CNN Architecture: 3-4 convolutional layers
- Training Data Size: 500-2000 play diagram images

## Follow-Up

1. How would you handle diagrams with varying levels of detail or different drawing styles?

2. Can you modify the model to identify multiple plays occurring simultaneously in a single diagram?

3. What techniques would you use to visualize which parts of the diagram the CNN focuses on for classification?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
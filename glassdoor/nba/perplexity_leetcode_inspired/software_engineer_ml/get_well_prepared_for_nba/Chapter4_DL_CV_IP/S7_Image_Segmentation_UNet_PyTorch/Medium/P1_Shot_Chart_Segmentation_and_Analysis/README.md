# NBA Shot Chart Segmentation and Analysis

## Problem Statement

Create a UNet-based model using PyTorch to segment and analyze shot charts for 
visualizing NBA player shooting patterns. The model should take as input a shot chart image 
and output a segmented image highlighting different shooting zones and efficiency areas.

## Examples

### Example 1

**Input:**

~~~yml
Input: Shot chart image of Stephen Curry's 2024-25 season (500x500 pixels, RGB)
~~~

**Output:**

~~~yml
Output: Segmented image with color-coded regions representing shooting efficiency
~~~

**Explanation:**

The model identifies high-efficiency areas (e.g., 3-point line, paint) with distinct colors, showcasing Curry's exceptional range and accuracy.


### Example 2

**Input:**

~~~yml
Input: Shot chart image of a center player's 2024-25 season (500x500 pixels, RGB)
~~~

**Output:**

~~~yml
Output: Segmented image highlighting close-range shots and post-up areas
~~~

**Explanation:**

The segmentation emphasizes the paint and low-post areas, reflecting the typical shooting pattern of a center.

### Example 3

**Input:**

~~~yml
Input: Comparative shot chart image of two guards (500x500 pixels, RGB)
~~~

**Output:**

~~~yml
Output: Segmented image showing overlapping and distinct shooting zones
~~~

**Explanation:**

The model segments areas where both players excel and areas of individual strength, facilitating direct comparison.


## Constraints


- Input Image Size: 500x500 pixels, RGB
- Output Segmentation Classes: 5 (e.g., high efficiency, medium efficiency, low efficiency, no shots, out of bounds)
- Model Architecture: UNet with skip connections
- Training Data: 1000-5000 annotated shot chart images
- Minimum Segmentation Accuracy: 85% IoU (Intersection over Union)

## Follow-Up

1. How would you modify the model to handle shot charts from different seasons or leagues with varying court dimensions?

2. Can you extend the model to provide quantitative analysis of shooting percentages for each segmented region?

3. What techniques would you use to ensure the model generalizes well to players with unique or evolving shooting patterns?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
# NBA Fan Segmentation: K-Means Clustering

## Problem Statement

Design a K-Means clustering algorithm using Scikit-learn to segment NBA fans
based on their engagement and purchasing behavior, aiming to identify distinct
fan groups for targeted marketing and personalized experiences.

## Examples

### Example 1

**Input:**

~~~yml
Fan Data: [Games Attended: 15, Merchandise Purchases: $500, App Usage (hours/week): 5, Social Media Interactions: 100]
~~~

**Output:**

~~~yml
Cluster: "High Engagement Superfan"

Centroid: [12, $450, 4.5, 80]
~~~

**Explanation:**

Fan shows high engagement across all metrics, indicating a dedicated supporter

### Example 2

**Input:**

~~~yml
Fan Data: [Games Attended: 2, Merchandise Purchases: $50, App Usage (hours/week): 1, Social Media Interactions: 10]
~~~

**Output:**

~~~yml
Cluster: "Casual Observer"

Centroid: [3, $75, 1.5, 15]
~~~

**Explanation:**

Fan demonstrates low engagement, suggesting occasional interest

### Example 3

**Input:**

~~~yml
Fan Data: [Games Attended: 0, Merchandise Purchases: $200, App Usage (hours/week): 8, Social Media Interactions: 150]
~~~

**Output:**

~~~yml
Cluster: "Digital Enthusiast"

Centroid: [1, $175, 7, 130]
~~~

**Explanation:**

Fan shows high digital engagement but low in-person attendance


## Constraints


- Input Features: 4-6 engagement and purchasing metrics
- Number of Clusters: 3-7
- Training Data Size: 1000-10000 fan records
- Feature Types: Numeric values representing engagement levels and purchases
- Normalization: StandardScaler for feature scaling

## Follow-Up

1. How would you determine the optimal number of clusters for fan segmentation?

2. Can you modify the model to handle categorical data like favorite player or preferred game day?

3. What techniques would you use to interpret and label the resulting clusters?

The implementation draws insights from the search results, particularly the research showing:

- The Orlando Magic's use of AI for fan segmentation and personalized experiences
- The application of K-means clustering in NBA player analysis, which can be adapted for fan segmentation
- The use of machine learning models to predict fan attitudes in sports sponsorship

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
# NBA Game Object Detection and Tracking

## Problem Statement

Implement a YOLO-based model using PyTorch to detect and track players, the ball, 
and referees in NBA game footage. The model should process video frames and 
output bounding boxes with class labels for each detected object.

## Examples

### Example 1

**Input:**

~~~yml
Input: Single frame from NBA game footage (1920x1080 RGB image)
~~~

**Output:**

~~~yml
Players: [(x1: 450, y1: 300, x2: 500, y2: 400, class: "player", team: "home", confidence: 0.95), ...]
Ball: [(x1: 960, y1: 540, x2: 980, y2: 560, class: "ball", confidence: 0.88)]
Referee: [(x1: 1200, y1: 700, x2: 1250, y2: 800, class: "referee", confidence: 0.92)]
~~~

**Explanation:**

The model detects multiple players, the ball, and a referee, providing bounding box coordinates and confidence scores.


### Example 2

**Input:**

~~~yml
Input: Video stream of NBA game (30 fps, 1280x720 resolution)
~~~

**Output:**

~~~yml
Sequence of detections for each frame
Tracking IDs for players to maintain identity across frames
~~~

**Explanation:**

The model processes each frame and maintains object identities across the video sequence.

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


- Input: Video frames (various resolutions, typically 720p or 1080p)
- Objects to detect: Players (home/away teams), ball, referees
- Model: YOLOv5 or YOLOv8 architecture
- Minimum detection confidence: 0.5
- Frame processing speed: At least 20 fps on GPU

## Follow-Up

1. How would you handle occlusions and fast movements typical in basketball games?

2. Can you modify the model to classify player actions (e.g., shooting, dribbling) in addition to detection?

3. What techniques would you use to improve tracking consistency across frames, especially for the fast-moving ball?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
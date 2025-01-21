# Automated Referee Foul Detection System

## Problem Statement

Design a deep learning model using PyTorch to detect and track referee movements and gestures in 
basketball game footage for automated foul detection. The model should process video frames, 
identify referees, track their movements, and recognize specific gestures associated with foul calls.

## Examples

### Example 1

**Input:**

~~~yml
Input: Video clip of a basketball game (1080p, 30 fps, 5 seconds)
~~~

**Output:**

~~~yml
Referee Tracking: [(frame_id: 1, ref_id: 1, x: 450, y: 300, gesture: "None"), ..., (frame_id: 150, ref_id: 1, x: 480, y: 320, gesture: "Foul_Call")]
~~~

**Explanation:**

The model tracks the referee's position across frames and detects a foul call gesture in the final frame.


### Example 2

**Input:**

~~~yml
Input: Video clip of a basketball game (720p, 60 fps, 3 seconds)
~~~

**Output:**

~~~yml
Referee Tracking: [(frame_id: 1, ref_id: 1, x: 200, y: 150, gesture: "Running"), ..., (frame_id: 180, ref_id: 1, x: 250, y: 200, gesture: "Blocking_Foul")]
~~~

**Explanation:**

The model tracks the referee moving across the court and identifies a specific blocking foul gesture.

### Example 3

**Input:**

~~~yml
Input: Video clip of a basketball game (1080p, 30 fps, 10 seconds)
~~~

**Output:**

~~~yml
Referee Tracking: [(frame_id: 1, ref_id: 1, x: 300, y: 400, gesture: "None"), (frame_id: 1, ref_id: 2, x: 800, y: 200, gesture: "None"), ..., (frame_id: 300, ref_id: 1, x: 350, y: 450, gesture: "Traveling_Violation")]
~~~

**Explanation:**

The model tracks multiple referees and detects a traveling violation gesture by one of them.


## Constraints


- Input: Video frames (720p or 1080p resolution)
- Output: Referee bounding boxes, tracking IDs, and gesture classifications
- Model Architecture: Faster R-CNN for detection, custom CNN for gesture recognition
- Minimum Detection Accuracy: 90% IoU for referee detection
- Gesture Recognition Accuracy: At least 85% for common foul gestures
- Real-time Processing: Achieve at least 20 fps on GPU

## Follow-Up

1. How would you handle occlusions when referees are temporarily blocked by players?

2. Can you extend the model to differentiate between different types of fouls based on referee gestures?

3. What techniques would you use to reduce false positives in foul detection?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A
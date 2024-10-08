# -*- coding: utf-8 -*-
"""Step3_path mapping and data export

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UqcXNlh8NGPnFGJZlc4ycnacTuYvJ1xz
"""



# Store movement path
movement_path = []

def draw_pose_landmarks(landmarks):
    # Get the center point of the person (e.g., the midpoint of hips)
    x, y = int(landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x * width), int(landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y * height)

    # Append to the movement path
    movement_path.append((x, y))

    # Draw the movement path on the 2D floor plan
    stroke(255, 0, 0)
    noFill()
    beginShape()
    for pos in movement_path:
        vertex(pos[0], pos[1])
    endShape()
This project is part of an ongoing research initiative, and we're opening it up to the community for feedback and collaboration. The goal is to enhance real-time human movement tracking using computer vision, and by making the code open source, we invite developers to contribute to optimizing and refining it. Your insights can help make this tool faster, smarter, and more efficient. Join us in pushing the boundaries of innovation!

## Phase 1: Camera Integration & Basic Room Detection
The first step is integrating the camera feed, detecting the edges of the room (walls, floor, ceiling), and generating a basic 2D room layout.

### 1. Camera Integration (Using OpenCV)
You’ll need OpenCV to capture the camera feed and process it within the Processing sketch. We can display this feed on the canvas and apply edge detection to identify the room's boundaries.
You can find the code in the repository titled in the file called "step1_camera_integration.py"

This code captures real-time video feed and applies Canny edge detection to visualize the boundaries of the room. From here, we can work on mapping these edges to construct a 2D floor plan.

### 2. Room Mapping & Floor Plan Creation
To create the floor plan, you can use OpenCV's edge detection to identify vertical and horizontal lines (walls, ceiling, and floor) in the image. You would process the detected edges, extract the spatial relationships, and draw them on the Processing canvas.

This would be an extension of the edge detection step, where you identify the largest connected lines and estimate the layout from them.

## Phase 2: Human Movement Tracking (Pose Detection with MediaPipe)
Once the room layout is detected, the next step is to track human movement. We can use MediaPipe's pose estimation model, which is lightweight and fast, suitable for real-time human pose tracking.

Setting up MediaPipe for Pose Detection
To track human movements, we can integrate MediaPipe for human pose detection.
The detailed code can be found in the repository in the file called "step2_camera_movement_tracking.py"

Here we use MediaPipe to process each video frame and extract pose landmarks. The landmarks can be used to track the movement of people within the room.

## Phase 3: Path Mapping & Data Export
In this phase, you will map the human movements onto the generated 2D floor plan, and store the movement data for analysis.

### Mapping Human Movements
We will map the detected human positions to a 2D floor plan by recording the (x, y) coordinates of the tracked human in real time and drawing lines representing their movement path.
The code for this stage can be found in the file called "step3_path_mapping_and_data_export.py"

### Data Logging & Export
We can log the movement data (coordinates and timestamps) and export it in CSV or JSON format.
This phase of the code is documented at "step3b_data_logging_and_export.py"

## Phase 4: User Interface (GUI)
For the GUI, Processing's own GUI tools (such as buttons and sliders) can be used, or you can integrate Tkinter or PyQt to create more advanced controls.
This part of the code can be found at "step4_interface_and_GUI.py"

## Phase 5: Optimization & Testing
For real-time performance, you can adjust frame rates, resolution, and apply multi-threading techniques to optimize the processing pipeline.
This phase is still in works.


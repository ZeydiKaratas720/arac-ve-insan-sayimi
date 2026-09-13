# People and Vehicle Counting Using YOLO

## 📌 Overview

This project is a real-time **People and Vehicle Counting System** developed using Python, YOLO, OpenCV, and ByteTrack.

The system processes a traffic video, detects people and vehicles, assigns tracking IDs to detected objects, and displays the number of people and vehicles in each video frame.

The project is designed as a practical **computer vision and intelligent traffic analysis** application.

---

## 🎯 Project Goal

The main goal of this project is to detect and count different object types in a traffic environment using a YOLO object detection model.

The system can detect:

* 👤 People
* 🚗 Cars
* 🏍️ Motorcycles
* 🚌 Buses
* 🚚 Trucks

The detected objects are tracked across video frames using **ByteTrack**.

---

## 🧠 How It Works

The system follows this pipeline:

```text
Input Traffic Video
        ↓
YOLO Object Detection
        ↓
Object Classification
        ↓
ByteTrack Object Tracking
        ↓
People / Vehicle Separation
        ↓
Counting
        ↓
Real-Time Visualization
```

YOLO detects the objects while ByteTrack helps maintain their identities between consecutive frames.

---

## 🚀 Features

* Real-time object detection
* People detection
* Vehicle detection
* Object tracking
* Unique tracking IDs
* People counting
* Vehicle counting
* Traffic video analysis
* Real-time visualization
* Support for multiple vehicle classes

---

## 🚗 Supported Vehicle Classes

The project uses the standard COCO class IDs:

| Class ID | Object     |
| -------: | ---------- |
|        0 | Person     |
|        2 | Car        |
|        3 | Motorcycle |
|        5 | Bus        |
|        7 | Truck      |

The system focuses on these five object categories.

---

## 🛠️ Technologies

* **Python**
* **YOLO**
* **Ultralytics**
* **ByteTrack**
* **OpenCV**

---

## 📦 Installation

Install the required libraries:

```bash id="a8k4gz"
pip install ultralytics opencv-python
```

---

## 📁 Project Structure

```text id="q2e5sp"
people-vehicle-counting/
│
├── counting.py
├── traffic.mp4
└── README.md
```

---

## ▶️ Running the Project

Place the traffic video in the project directory:

```text id="0i1zjz"
traffic.mp4
```

Then run:

```bash id="4ax7od"
python counting.py
```

The video will open in a new OpenCV window.

Press:

```text id="7ayqxi"
Q
```

to exit the application.

---

## 💻 Core Implementation

The YOLO model is initialized with:

```python id="e5g3jh"
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
```

The video is opened using OpenCV:

```python id="f1wz4d"
video = cv2.VideoCapture("traffic.mp4")
```

YOLO tracking is performed using ByteTrack:

```python id="2c4n3b"
results = model.track(
    frame,
    persist=True,
    tracker="bytetrack.yaml",
    classes=[0, 2, 3, 5, 7],
    verbose=False
)
```

The `persist=True` parameter allows the tracker to maintain object identities between frames.

---

## 👤 People Counting

People are identified using the COCO class ID `0`.

```python id="70h3bc"
if class_id == 0:
    person_count += 1
```

The number of detected people is then displayed on the video:

```text id="clbqne"
People: 12
```

---

## 🚘 Vehicle Counting

Vehicles are identified using the following class IDs:

```python id="2c3n8j"
CAR = 2
MOTORCYCLE = 3
BUS = 5
TRUCK = 7
```

The system counts these objects as vehicles:

```python id="8eqv7u"
elif class_id in [2, 3, 5, 7]:
    vehicle_count += 1
```

Example output:

```text id="p8kzv0"
Vehicles: 27
```

---

## 🆔 Object Tracking

ByteTrack assigns a tracking ID to detected objects.

For example:

```text id="6k5m3h"
Person → ID 1
Car → ID 2
Car → ID 3
Bus → ID 4
Person → ID 5
```

This allows objects to be tracked as they move through the scene.

---

## 📊 Example Output

The processed video displays the detected objects together with the current counts:

```text id="j9yq2u"
People: 12
Vehicles: 27
```

Each detected object is also displayed with its bounding box and tracking information.

---

## 🔍 Detection vs Tracking

### Object Detection

YOLO identifies objects in each frame:

```text id="1x9s5b"
Frame 1 → Car, Person, Bus
Frame 2 → Car, Person, Bus
Frame 3 → Car, Person, Bus
```

### Object Tracking

ByteTrack attempts to maintain the same identity:

```text id="r5x3mt"
Car → ID 1
Car → ID 1
Car → ID 1
```

This is especially useful for traffic monitoring and object counting.

---

## 🔮 Future Improvements

The current project can be extended into a more advanced traffic monitoring system.

### 1. Line-Crossing Counting

Instead of counting objects visible in each frame, a virtual line can be placed on the road.

```text id="7f1k3z"
             ROAD

       ↓ Car ID 12

========================
       COUNT LINE
========================

       ↓ Car ID 12

Total Cars Passed: 25
```

Each object would be counted only once when it crosses the line.

### 2. Direction Detection

The system could determine whether vehicles are moving:

```text id="0f2b5h"
Incoming → 15 vehicles
Outgoing → 21 vehicles
```

### 3. Vehicle-Type Statistics

The system could provide detailed traffic statistics:

```text id="7t5x3n"
Cars:        32
Motorcycles: 8
Buses:       4
Trucks:      6
People:      17
```

### 4. Traffic Density

Traffic density could be classified as:

```text id="4qv7zc"
Low
Medium
High
```

based on the number of detected vehicles.

### 5. Speed Estimation

Object tracking can be combined with camera calibration and distance estimation to calculate approximate vehicle speed.

### 6. Data Logging

Traffic statistics could be saved into CSV files:

```text id="1n9m4e"
Time, Cars, Buses, Trucks, Motorcycles, People
10:00, 12, 2, 1, 3, 8
10:01, 15, 2, 2, 4, 10
```

This would allow traffic data to be analyzed later.

---

## ⚠️ Limitations

Counting objects in every frame does **not** represent the total number of unique objects that passed through the scene.

For example, the same car may appear in many consecutive frames.

ByteTrack helps maintain object identities, but a more advanced counting system should use **line-crossing or region-based counting** to count each object only once.

Performance can also be affected by:

* Camera angle
* Lighting conditions
* Object occlusion
* Video resolution
* Heavy traffic
* Small or distant objects
* Fast-moving vehicles

---

## 📌 Applications

This type of computer vision system can be used for:

* Smart city systems
* Traffic monitoring
* Vehicle flow analysis
* Road safety systems
* Parking management
* Traffic density estimation
* Intelligent transportation systems
* Security monitoring
* Urban mobility analysis

---

## 🎓 Learning Outcomes

This project provides practical experience with:

* Object detection
* Object tracking
* Computer vision
* Video processing
* YOLO
* ByteTrack
* OpenCV
* Real-time data analysis
* Traffic monitoring

---

## 🔮 Future Project Direction

A more advanced version of this project could combine:

```text id="5h8s4n"
YOLO
  +
ByteTrack
  +
Line Crossing
  +
Vehicle Classification
  +
Speed Estimation
  +
Traffic Density
  +
Data Visualization
```

to create a complete **AI-Based Traffic Monitoring System**.

---

## 👩‍💻 Author

**Dilara Karataş**

Computer Engineering Student
Interested in Computer Vision, Artificial Intelligence and Embedded Systems.

---

## ⭐ Project Purpose

This project was developed as a practical computer vision application to explore how **YOLO object detection and ByteTrack object tracking can be used to analyze people and vehicle traffic in real-world video data**.

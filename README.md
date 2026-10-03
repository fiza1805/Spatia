# Spatia — AI powered Space understanding & Interior Planning Assistant

Spatia is an AI based room analysis project which uses computer vision to understand the room through a video and come up with meaningful suggestions for interior and space planning based on the user's budget.

## What it Does

The prototype works in the following way

Room Video → OpenCV → YOLO Object detection → Room Analysis → Budget Based Recommendations → JSON Response

The project takes a room video as input, samples some of the video's frames, detects the objects in these sampled frames with YOLO, and recommends space planning and interior suggestions.

## Features provided

🎥Video room analysis

🧠YOLO Object detection
📊Objects tracking in sampled video frames

💰Budget based recommendations

🚀FastAPI backend for room analysis

📋Analysis in JSON format

🌐FastAPI interactive docs at /docs
## Technologies Used
Python
YOLO / Ultralytics
OpenCV
FastAPI
Uvicorn
Streamlit

## Project Structure
```text
.
├── backend/
│  ├── analyzer.py
│  └── api.py
├── detect.py
├── main.py
├── recommendations.py
├── room_analysis.py
├── room_understanding.py
├── spacial_analysis.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```
## How it Works
### 1. Room Video
User provides the video of the room to the FastAPI endpoint
### 2. Video Frame Sampling
OpenCV reads the video, and samples some of the video's frame for further processing instead of processing all of the video's frames
### 3. Object Detection
YOLO does object detection on the sampled frames and detects objects like beds, chairs, laptop, and anything else detectable by YOLO.
### 4. Room Analysis
We gather the information about objects detected by YOLO along with their confidence and make an analysis about the room
### 5. Budget Based Recommendations
We use the objects detected and the budget provided by the user to make recommendations about the room.
### 6. API response
The FastAPI returns a JSON response with the analysis of the room.
Example:
```json
{
"success": true,
"analysis": {
"room_type": "Bedroom",
"object_count": 3,
"budget": 10000,
"recommendations": []
}
}
```
## How to Run the Project
### 1. Clone the Repo
```bash
git clone https://github.com/fiza1805/Spatia.git
cd Spatia
```
### 2. Install Requirements
```bash
pip install -r requirements.txt
```
### 3. Start the Server
```bash
uvicorn backend.api:app --reload
```
### 4. Open the Server
Go to the following URL in your browser
```text
http://127.0.0.1:8000
```
Documentation is available at
```text
http://127.0.0.1:8000/docs
```
## Example Use Case
User provides a video of a bedroom and a budget of say ₹10,000
Spatia will return recommendations like
making study area if possible
keeping a walking pathway
making sure seats are placed near study area
avoiding keeping heavy budget objects
making some changes in the room with the remaining budget

## Project Status
Status: Working Prototype

The current prototype implements the Python and computer vision part of the project. The future updates may focus on improving the room understanding and making better suggestions with a more comprehensive UI.

## Author

## Sumaiya

B.Tech - Computer Science & Engineering (AI & Data Science)

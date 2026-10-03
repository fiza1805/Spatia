import os
import cv2
from ultralytics import YOLO


MODEL_PATH = "yolo11s.pt"


class SpatiaAnalyzer:

    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def analyze_video(self, video_path: str, budget: int):

        video = cv2.VideoCapture(video_path)

        if not video.isOpened():
            raise ValueError("Could not open the uploaded video.")

        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = video.get(cv2.CAP_PROP_FPS)

        if fps <= 0:
            fps = 30

        duration = total_frames / fps

        # Analyze approximately 15 frames across the video.
        sample_count = min(15, max(1, total_frames))
        frame_indices = [
            int(i * total_frames / sample_count)
            for i in range(sample_count)
        ]

        detected_objects = {}

        for frame_index in frame_indices:

            video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

            success, frame = video.read()

            if not success:
                continue

            results = self.model(
                frame,
                conf=0.25,
                verbose=False
            )

            for result in results:

                if result.boxes is None:
                    continue

                for box in result.boxes:

                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    object_name = result.names[class_id]

                    if object_name not in detected_objects:

                        detected_objects[object_name] = {
                            "frames_seen": 0,
                            "max_confidence": 0.0
                        }

                    detected_objects[object_name]["frames_seen"] += 1

                    detected_objects[object_name]["max_confidence"] = max(
                        detected_objects[object_name]["max_confidence"],
                        confidence
                    )

        video.release()

        objects = []

        for name, data in detected_objects.items():

            objects.append({
                "name": name,
                "frames_seen": data["frames_seen"],
                "confidence": round(data["max_confidence"], 2)
            })

        recommendations = self.generate_recommendations(
            detected_objects,
            budget
        )

        return {
            "room_type": "Bedroom",
            "duration_sec": round(duration, 1),
            "objects": objects,
            "object_count": len(objects),
            "budget": budget,
            "recommendations": recommendations
        }

    def generate_recommendations(self, objects, budget):

        recommendations = []

        names = set(objects.keys())

        # Workspace
        if "laptop" in names:

            if budget <= 5000:
                recommendations.append({
                    "category": "WORKSPACE",
                    "title": "Create a low-cost study zone",
                    "description":
                        "Keep the laptop in one dedicated area and "
                        "organize charging cables to reduce clutter.",
                    "estimated_cost": 500
                })

            elif budget <= 10000:
                recommendations.append({
                    "category": "WORKSPACE",
                    "title": "Upgrade your study area",
                    "description":
                        "Consider a compact desk or wall-mounted workspace "
                        "for a more comfortable laptop setup.",
                    "estimated_cost": 3500
                })

            else:
                recommendations.append({
                    "category": "WORKSPACE",
                    "title": "Build a dedicated study zone",
                    "description":
                        "Create a dedicated workspace with a compact desk, "
                        "comfortable chair and organized cable management.",
                    "estimated_cost": 8000
                })

        # Bed
        if "bed" in names:

            recommendations.append({
                "category": "BED ARRANGEMENT",
                "title": "Maintain a clear walking path",
                "description":
                    "Keep sufficient space around the bed so movement "
                    "through the room remains comfortable.",
                "estimated_cost": 0
            })

        # Chair
        if "chair" in names:

            recommendations.append({
                "category": "SEATING",
                "title": "Position the chair near the workspace",
                "description":
                    "Place the chair where it can be used comfortably "
                    "without blocking the main walking path.",
                "estimated_cost": 0
            })

        # Cupboard
        if "cupboard" in names:

            recommendations.append({
                "category": "STORAGE",
                "title": "Keep storage accessible",
                "description":
                    "Maintain enough clearance in front of the cupboard "
                    "so the doors can open comfortably.",
                "estimated_cost": 0
            })

        # Small budget
        if budget <= 5000:

            recommendations.append({
                "category": "BUDGET",
                "title": "Prioritize rearrangement over new furniture",
                "description":
                    "With a ₹5,000 budget, focus on decluttering, "
                    "rearranging existing furniture and inexpensive "
                    "lighting or organization improvements.",
                "estimated_cost": 2000
            })

        elif budget <= 10000:

            recommendations.append({
                "category": "BUDGET",
                "title": "Make targeted upgrades",
                "description":
                    "Use your budget for one or two meaningful upgrades "
                    "while reusing your existing furniture.",
                "estimated_cost": 7500
            })

        elif budget <= 15000:

            recommendations.append({
                "category": "BUDGET",
                "title": "Combine layout changes with upgrades",
                "description":
                    "Your budget allows a combination of furniture "
                    "improvements, lighting and organization upgrades.",
                "estimated_cost": 12000
            })

        else:

            recommendations.append({
                "category": "BUDGET",
                "title": "Plan a larger room refresh",
                "description":
                    "You can consider new furniture or larger interior "
                    "changes while keeping the existing layout practical.",
                "estimated_cost": 20000
            })

        return recommendations


analyzer = SpatiaAnalyzer()
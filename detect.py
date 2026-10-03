from ultralytics import YOLO
import glob
import re

# Load YOLO model
model = YOLO("yolo11s.pt")

# Get all frames
frames = glob.glob("bedroom_frames/*.jpg")

# Sort frames correctly: frame_0, frame_1, frame_2...
def frame_number(path):
    return int(re.search(r"frame_(\d+)", path).group(1))

frames = sorted(frames, key=frame_number)

print(f"Found {len(frames)} frames\n")

# Store objects that we track
tracked_objects = {}

for frame in frames:

    results = model.track(
        frame,
        persist=True,
        conf=0.25,
        verbose=False
    )

    print(f"\n{frame}")

    for result in results:

        if result.boxes.id is None:
            continue

        track_ids = result.boxes.id.int().tolist()

        for box, track_id in zip(result.boxes, track_ids):

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            object_name = result.names[class_id]

            print(
                f"  {object_name} "
                f"| ID: {track_id} "
                f"| Confidence: {confidence:.2f}"
            )

            # Store information
            if track_id not in tracked_objects:

                tracked_objects[track_id] = {
                    "object": object_name,
                    "frames_seen": 0
                }

            tracked_objects[track_id]["frames_seen"] += 1


print("\n==============================")
print("SPATIA ROOM OBJECTS")
print("==============================")

for track_id, data in tracked_objects.items():

    print(
        f"ID {track_id}: "
        f"{data['object']} "
        f"→ seen in {data['frames_seen']} frames"
    )
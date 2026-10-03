from ultralytics import YOLO
import os
from collections import defaultdict

model = YOLO("yolo11s.pt")

object_data = defaultdict(list)

print("\n" + "=" * 55)
print("              SPATIA")
print("       AI ROOM UNDERSTANDING")
print("=" * 55)

print("\nAnalyzing bedroom...\n")

for frame_number in range(15):

    filename = f"bedroom_frames/frame_{frame_number}.jpg"

    if not os.path.exists(filename):
        continue

    results = model(
        filename,
        conf=0.35,
        verbose=False
    )

    print(f"Frame {frame_number}:")

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            object_name = result.names[class_id]

            object_data[object_name].append(
                {
                    "frame": frame_number,
                    "confidence": confidence
                }
            )

            print(
                f"  {object_name} "
                f"(confidence: {confidence:.2f})"
            )


# -----------------------------------------
# ROOM INVENTORY
# -----------------------------------------

print("\n")
print("=" * 55)
print("          SPATIA ROOM INVENTORY")
print("=" * 55)

for object_name, detections in object_data.items():

    frames = sorted(
        set(d["frame"] for d in detections)
    )

    average_confidence = sum(
        d["confidence"] for d in detections
    ) / len(detections)

    print(f"\n{object_name}")
    print(f"  Seen in frames     : {frames}")
    print(f"  Detections         : {len(detections)}")
    print(
        f"  Average confidence : "
        f"{average_confidence:.2f}"
    )

print("\n" + "=" * 55)
print("          ANALYSIS COMPLETE")
print("=" * 55)
import cv2
import os

video = cv2.VideoCapture("bedroom.mp4")

if not video.isOpened():
    print("Could not open bedroom video.")
    exit()

print("Bedroom video opened successfully!")

os.makedirs("bedroom_frames", exist_ok=True)

frame_count = 0
saved_count = 0

while True:
    success, frame = video.read()

    if not success:
        break

    frame_count += 1

    # Save every 30th frame
    if frame_count % 30 == 0:
        filename = f"bedroom_frames/frame_{saved_count}.jpg"

        cv2.imwrite(filename, frame)

        saved_count += 1

video.release()

print(f"Total frames read: {frame_count}")
print(f"Frames saved: {saved_count}")
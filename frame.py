import os
import cv2

def extract_frames(video_path, output_folder):
    # Make sure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    count = 0
    # Read the video
    for vdo in os.listdir(video_path):
    #vdo = ''
        if not vdo.startswith(".ipy"):
            cap = cv2.VideoCapture(video_path)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            while cap.isOpened():
                ret, frame = cap.read()

                if ret:
                    cv2.imwrite(os.path.join(output_folder, f"frame_{count}.jpg"), frame)
                    count += 1
                else:
                    break

                # Optionally, you can print progress
                print(f"Extracting frame {count}")

        # Release the VideoCapture object
        cap.release()
    
# Path to your video
video_path = 'UCF50/TaiChi/'

# Folder where you want to save the frames
output_folder = 'tai_chi/class'

# Extract frames
extract_frames(video_path, output_folder)
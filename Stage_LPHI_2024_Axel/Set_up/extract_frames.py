import subprocess
import os
import cv2

def extract_frames(video_path, output_folder, fps=10):
    """
    Extract frames from an MP4 video and save them as PNG images with a fixed resolution.
    Ensures uniform frame size by resizing and padding if needed.

    :param video_path: Path to the input MP4 video file.
    :param output_folder: Path to the folder where frames will be saved.
    :param fps: Frames per second to extract.
    """
    video = cv2.VideoCapture(video_path)

    # Get width and height
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    output_pattern = os.path.join(output_folder, "frame_%03d.png")
    
    command = [
        "ffmpeg",
        "-i", video_path,  # Input video
        "-vf", f"fps={fps},scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2",
        "-q:v", "2",  # Quality setting for PNG
        output_pattern  # Output file pattern
    ]
    
    subprocess.run(command, check=True)
    print(f"Frames saved in {output_folder} with resolution {width}x{height}")
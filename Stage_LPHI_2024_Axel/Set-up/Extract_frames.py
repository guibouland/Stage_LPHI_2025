import subprocess
import os

def extract_frames(video_path, output_folder, fps=10, width=1605, height=1541):
    """
    Extract frames from an MP4 video and save them as PNG images with a fixed resolution.
    Ensures uniform frame size by resizing and padding if needed.

    :param video_path: Path to the input MP4 video file.
    :param output_folder: Path to the folder where frames will be saved.
    :param fps: Frames per second to extract.
    :param width: Output frame width.
    :param height: Output frame height.
    """

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    output_pattern = os.path.join(output_folder, "frame_%04d.png")
    
    command = [
        "ffmpeg",
        "-i", video_path,  # Input video
        "-vf", f"fps={fps},scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2",
        "-q:v", "2",  # Quality setting for PNG
        output_pattern  # Output file pattern
    ]
    
    subprocess.run(command, check=True)
    print(f"Frames saved in {output_folder} with resolution {width}x{height}")

# Example usage
extract_frames(
    "/home/gbouland/Stage-LPHI-2024/input/norma/vert/250210-Norma-GC-cut-3hpA-green channel_Fish_1.mp4", 
    "/home/gbouland/Stage-LPHI-2024/input/norma/vert/frames", 
    fps=10, width=1605, height=1541
)

import cv2

def get_frame_count(video_path):
    """
    Get the total number of frames in a video.
    Args:
        video_path (str): The path to the video file.
    Returns:
        int: The total number of frames in the video.
    """

    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return frame_count
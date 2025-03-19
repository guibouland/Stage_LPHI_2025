import os
import zipfile
from count import get_frame_count

def empty_dataset_testy_zip(testy_folder, video_path):
    """
    Function that creates empty zip files.

    Parameters
    ----------
    testy_folder : str
        The path to the folder where the zip files will be created or are stored. Should be the length of the video (in frames).
    video_path : str
        The path to the video file.
    """
    
    folder_path = os.path.dirname(os.path.realpath(__file__))
    parent_folder = os.path.dirname(folder_path)
    testy_path = os.path.join(parent_folder, testy_folder)
    os.makedirs(testy_path, exist_ok=True)

    n = get_frame_count(video_path)

    # Create n empty zip files
    for i in range(n):
        zip_filename = os.path.join(testy_path, f'{i:03d}_masks.zip')
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            pass 
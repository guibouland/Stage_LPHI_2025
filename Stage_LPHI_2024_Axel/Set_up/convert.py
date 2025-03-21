import os
from time import time
from moviepy.editor import VideoFileClip

def convert_avi_to_mp4(avi_file_path):
    """
    Converts an AVI video file to MP4 format.
    Args:
        avi_file_path (str): The file path of the AVI video to be converted.
    Raises:
        FileNotFoundError: If the specified AVI file does not exist.
    Returns:
        A new MP4 video file with the same name as the AVI file in the same directory.
    Example:
        convert_avi_to_mp4('/path/to/video.avi')
    """

    # function guard
    if not os.path.exists(avi_file_path):
        raise FileNotFoundError(avi_file_path)
    t0 = time()
    clip = VideoFileClip(avi_file_path)
    path, file_name = os.path.split(avi_file_path)
    output_name = os.path.join(path, os.path.splitext(file_name)[0] + '.mp4')
    clip.write_videofile(output_name)
    print('Finished conversion in %is' % (time() - t0))

def convert_all_avi_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.avi'):
                avi_file_path = os.path.join(root, file_name)
                convert_avi_to_mp4(avi_file_path)


# Delete avi files in folder and subfolders
def delete_avi_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.avi'):
                avi_file_path = os.path.join(root, file_name)
                os.remove(avi_file_path)



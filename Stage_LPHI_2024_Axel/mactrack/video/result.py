import os
import cv2
import numpy as np
import random

def draw_contours(image, contours, number, colors):
    color = colors[number % len(colors)]
    for contour in contours:
        cv2.drawContours(image, [contour], -1, color, 2)
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = contour[0][0]
        cv2.putText(image, str(number), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 2)

def generate_random_rgb_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def result(input_folder):
    input_folder_v = os.path.join(input_folder, 'vert/frames')
    output_folder_v = 'output/resultv'
    list_track_folder_v = 'output/list_track'
    os.makedirs(output_folder_v, exist_ok=True)    
    input_folder = os.path.join(input_folder, 'dataset/test/test_x')
    output_folder = 'output/result'
    list_track_folder = 'output/list_track'
    os.makedirs(output_folder, exist_ok=True)

    colors = [generate_random_rgb_color() for _ in range(100)]

    for image_file in os.listdir(input_folder):
        if image_file.endswith('_image.png'):
            a = image_file.split('_')[0].zfill(3)
            a_number = int(a)
            image_path = os.path.join(input_folder, image_file)
            original_image = cv2.imread(image_path)
            image_copy = original_image.copy()

            for macrophage_dir in os.listdir(list_track_folder):
                if macrophage_dir.startswith('macrophage_'):
                    b_number = int(macrophage_dir.split('_')[1])
                    macrophage_path = os.path.join(list_track_folder, macrophage_dir)

                    for track_image_file in os.listdir(macrophage_path):
                        c, d = track_image_file.split('_')[:2]
                        c_number = int(c)

                        if c_number == a_number:
                            track_image_path = os.path.join(macrophage_path, track_image_file)
                            track_image = cv2.imread(track_image_path, cv2.IMREAD_GRAYSCALE)
                            contours, _ = cv2.findContours(track_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                            draw_contours(image_copy, contours, b_number, colors)
            output_image_path = os.path.join(output_folder, f"{a}_with_all_macrophages.png")
            cv2.imwrite(output_image_path, image_copy)

    for image_file in os.listdir(input_folder_v):
            if image_file.endswith('_image.png'):
                a = image_file.split('_')[0].zfill(3)
                a_number = int(a)
                image_path = os.path.join(input_folder_v, image_file)
                original_image = cv2.imread(image_path)
                image_copy = original_image.copy()

                for macrophage_dir in os.listdir(list_track_folder_v):
                    if macrophage_dir.startswith('macrophage_'):
                        b_number = int(macrophage_dir.split('_')[1])
                        macrophage_path = os.path.join(list_track_folder_v, macrophage_dir)

                        for track_image_file in os.listdir(macrophage_path):
                            c, d = track_image_file.split('_')[:2]
                            c_number = int(c)

                            if c_number == a_number:
                                track_image_path = os.path.join(macrophage_path, track_image_file)
                                track_image = cv2.imread(track_image_path, cv2.IMREAD_GRAYSCALE)
                                contours, _ = cv2.findContours(track_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                                draw_contours(image_copy, contours, b_number, colors)
                output_image_path = os.path.join(output_folder_v, f"{a}_with_all_macrophages.png")
                cv2.imwrite(output_image_path, image_copy)

def video():
    result_folder = 'output/result'
    video_output = 'output/result_video.mp4'
    images = [img for img in os.listdir(result_folder) if img.endswith('.png')]
    images.sort()  

    if not images:
        raise ValueError("Aucune image trouvée dans le dossier 'output/result'.")

    first_image_path = os.path.join(result_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
    video = cv2.VideoWriter(video_output, fourcc, 10.0, (width, height))

    for image in images:
        image_path = os.path.join(result_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    video.release()
    cv2.destroyAllWindows()
    print(f"Vidéo créée avec succès : {video_output}")

    result_folder = 'output/resultv'
    video_output = 'output/result_video_v.mp4'
    images = [img for img in os.listdir(result_folder) if img.endswith('.png')]
    images.sort()  

    if not images:
        raise ValueError("Aucune image trouvée dans le dossier 'output/result'.")

    first_image_path = os.path.join(result_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
    video = cv2.VideoWriter(video_output, fourcc, 10.0, (width, height))

    for image in images:
        image_path = os.path.join(result_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    video.release()
    cv2.destroyAllWindows()
    print(f"Vidéo créée avec succès : {video_output}")

def videocomp():
    image_folder = 'output/list_comp'
    video_name = 'output/result_video_w.mp4'
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_name, fourcc, 10.0, (width, height))

    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    video.release()
    cv2.destroyAllWindows()
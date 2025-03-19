import os
import csv

def create_dataset_csv(input_folder, output_csv):
    """
    Creates a CSV file listing image files and their corresponding label files for training and testing datasets.
    Args:
        input_folder (str): The path to the input folder containing 'train' and 'test' subdirectories.
        output_csv (str): The path to the output CSV file to be created.
    The CSV file will have three columns:
        - 'input': The relative path to the image file.
        - 'label': The relative path to the label file.
        - 'set': The dataset type ('training' or 'testing').
    The function assumes the following directory structure within the input folder:
        input_folder/
        ├── train/
        │   ├── train_x/  # Contains training images (e.g., .png, .jpg)
        │   └── train_y/  # Contains training labels (e.g., .zip)
        └── test/
            ├── test_x/  # Contains testing images (e.g., .png, .jpg)
            └── test_y/  # Contains testing labels (e.g., .zip)
    """

    train_x_folder = os.path.join(input_folder, 'train/train_x')
    train_y_folder = os.path.join(input_folder, 'train/train_y')
    test_x_folder = os.path.join(input_folder, 'test/test_x')
    test_y_folder = os.path.join(input_folder, 'test/test_y')
    
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['input', 'label', 'set'])
        
        # Process training data
        train_x_files = sorted([f for f in os.listdir(train_x_folder) if f.endswith(('.png', '.jpg'))])
        train_y_files = sorted([f for f in os.listdir(train_y_folder) if f.endswith('.zip')])
        
        for x_file, y_file in zip(train_x_files, train_y_files):
            writer.writerow([os.path.join('train/train_x', x_file), os.path.join('train/train_y', y_file), 'training'])
        
        # Process testing data
        test_x_files = sorted([f for f in os.listdir(test_x_folder) if f.endswith(('.png', '.jpg'))])
        test_y_files = sorted([f for f in os.listdir(test_y_folder) if f.endswith('.zip')])
        
        for x_file, y_file in zip(test_x_files, test_y_files):
            writer.writerow([os.path.join('test/test_x', x_file), os.path.join('test/test_y', y_file), 'testing'])
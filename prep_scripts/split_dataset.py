import os
import random
import shutil

'''
Script for splitting a dataset into train, validation and test sets.
'''

# Configurations
source_dir = 'C:\\Users\\píchau\\Documents\\TCC\\imagens'
output_dir = 'C:\\Users\\píchau\\Documents\\TCC\\dataset'
train_split = 0.7  # 70% para treino
val_split = 0.15    # 15% para validação
test_split = 0.15   # 15% para teste

# Function to create directories
def create_dirs(output_dir):
    for folder in ['train', 'val', 'test']:
        os.makedirs(os.path.join(output_dir, 'images', folder), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'labels', folder), exist_ok=True)

# Function to split the dataset into three sets: train, validation and test
def split_dataset(source_dir, output_dir, train_split, val_split, test_split):
    images = [f for f in os.listdir(source_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    random.shuffle(images)
    
    # Defining the sizes of each set
    train_size = int(train_split * len(images))
    val_size = int(val_split * len(images))
    
    # Dividing the images into the sets
    train_images = images[:train_size]
    val_images = images[train_size:train_size + val_size]
    test_images = images[train_size + val_size:]
    
    # Moving the images and their corresponding annotation files
    for image_set, folder in zip([train_images, val_images, test_images], ['train', 'val', 'test']):
        for image in image_set:
            # Origin and destination paths
            src_image_path = os.path.join(source_dir, image)
            dst_image_path = os.path.join(output_dir, 'images', folder, image)
            
            # Moving the image file
            shutil.copy(src_image_path, dst_image_path)
            
            # Also moving the annotation file
            label_file = image.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt')
            src_label_path = os.path.join(source_dir, label_file)
            dst_label_path = os.path.join(output_dir, 'labels', folder, label_file)
            
            if os.path.exists(src_label_path):
                shutil.copy(src_label_path, dst_label_path)

if __name__ == "__main__":
    # Create directories
    create_dirs(output_dir)
    
    # Divide and move the images
    split_dataset(source_dir, output_dir, train_split, val_split, test_split)

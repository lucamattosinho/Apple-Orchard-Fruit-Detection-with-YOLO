import os

'''
Calculates the Intersection over Union (IoU) between ground truths and predictions.
'''

def calculate_global_iou(iou_results):
    """
    Calculates the global IoU from a dictionary of IoU results.
    """
    total_iou = 0
    total_ground_truths = 0

    for file_name, iou_list in iou_results.items():
        total_iou += sum(iou_list)  # Sum of IoUs
        total_ground_truths += len(iou_list)  # Number of ground truths

    if total_ground_truths == 0:
        return 0  # Avoid division by zero

    return total_iou / total_ground_truths

def load_boxes_from_txt(file_path):
    """
    Reads a list of boxes from a text file.
    Returns a list of tuples (class_id, x_center, y_center, width, height).
    """
    boxes = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            class_id = int(parts[0])
            x_center, y_center, width, height = map(float, parts[1:])
            boxes.append((class_id, x_center, y_center, width, height))
    return boxes

def convert_to_absolute(box, img_width, img_height):
    """
    Converts a box from relative coordinates to absolute coordinates.
    """
    class_id, x_center, y_center, width, height = box
    x_min = (x_center - width / 2) * img_width
    y_min = (y_center - height / 2) * img_height
    x_max = (x_center + width / 2) * img_width
    y_max = (y_center + height / 2) * img_height
    return class_id, x_min, y_min, x_max, y_max

def calculate_iou(box1, box2):
    """
    Calculates the Intersection over Union (IoU) between two boxes.
    """
    x_min_inter = max(box1[0], box2[0])
    y_min_inter = max(box1[1], box2[1])
    x_max_inter = min(box1[2], box2[2])
    y_max_inter = min(box1[3], box2[3])

    inter_width = max(0, x_max_inter - x_min_inter)
    inter_height = max(0, y_max_inter - y_min_inter)
    inter_area = inter_width * inter_height

    area_box1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area_box2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union_area = area_box1 + area_box2 - inter_area

    return inter_area / union_area if union_area > 0 else 0

def calculate_iou_for_directories(labels_dir, preds_dir, img_width=640, img_height=480):
    """
    Calculates the Intersection over Union (IoU) between ground truths and predictions.
    """
    results = {}
    for gt_file in os.listdir(labels_dir):
        gt_path = os.path.join(labels_dir, gt_file)
        pred_path = os.path.join(preds_dir, gt_file)

        if not os.path.exists(pred_path):
            print(f"A previsão para {gt_file} não foi encontrada em {preds_dir}.")
            continue

        gt_boxes = load_boxes_from_txt(gt_path)
        pred_boxes = load_boxes_from_txt(pred_path)

        iou_list = []
        for gt_box in gt_boxes:
            gt_abs = convert_to_absolute(gt_box, img_width, img_height)
            best_iou = 0
            for pred_box in pred_boxes:
                pred_abs = convert_to_absolute(pred_box, img_width, img_height)
                iou = calculate_iou(gt_abs[1:], pred_abs[1:])  # Ignorar class_id
                best_iou = max(best_iou, iou)
            iou_list.append(best_iou)

        results[gt_file] = iou_list

    return results

# Directories with ground truths and predictions
labels_dir = "C:/Users/píchau/Documents/TCC/dataset/labels/test_preprocessed"       # ground truth directory
preds_dir = "C:/Users/píchau/Documents/TCC/yolov8-env/runs/test/test_11_hb/labels"   # predictions directory

# Image dimensions 
img_width = 1024
img_height = 1024

# IoU calculation
iou_results = calculate_iou_for_directories(labels_dir, preds_dir, img_width, img_height)

# Global IoU calculation
global_iou = calculate_global_iou(iou_results)

# Display individual results
for file_name, iou_list in iou_results.items():
    print(f"{file_name}: IoUs = {iou_list}")
    
# Display global IoU
print(f"IoU global: {global_iou}")

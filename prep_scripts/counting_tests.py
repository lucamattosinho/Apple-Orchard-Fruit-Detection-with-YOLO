import os

def calculate_count_metrics(labels_dir, predictions_dir):
    """
    Calculates the Mean Absolute Error (MAE) and Mean Absolute Percentage Error (MAPE) for object counting.
    
    labels_dir: Directory with the ground truth files.
    predictions_dir: Directory with the prediction files.
    
    Returns:
    - MAE: Mean Absolute Error
    - MAPE: Mean Absolute Percentage Error
    """
    total_absolute_error = 0
    total_percentage_error = 0
    total_images = 0

    # Iterate over the label files
    for label_file in os.listdir(labels_dir):
        label_path = os.path.join(labels_dir, label_file)
        prediction_path = os.path.join(predictions_dir, label_file)

        # Verifies if the prediction file exists
        if not os.path.exists(prediction_path):
            continue

        # Count the number of real and predicted objects
        with open(label_path, "r") as lf:
            num_real = len(lf.readlines())  # Number of real apples
        
        with open(prediction_path, "r") as pf:
            num_predicted = len(pf.readlines())  # Number of predicted apples

        # Calculates the errors
        absolute_error = abs(num_real - num_predicted)
        percentage_error = (absolute_error / num_real) * 100 if num_real > 0 else 0

        # Accumulates the errors
        total_absolute_error += absolute_error
        total_percentage_error += percentage_error
        total_images += 1

    # Calculates the metrics
    mae = total_absolute_error / total_images if total_images > 0 else 0
    mape = total_percentage_error / total_images if total_images > 0 else 0

    return mae, mape


# Directories with the ground truth and prediction files
labels_dir = "C:/Users/píchau/Documents/TCC/dataset/labels/test"       # ground truth directory
preds_dir = "C:/Users/píchau/Documents/TCC/yolov8-env/runs/detect/predict2/labels"   # prediction directory

# Calculates the metrics
mae, mape = calculate_count_metrics(labels_dir, preds_dir)

# Displays the results
print(f"Erro Absoluto Médio (MAE): {mae:.2f}")
print(f"Erro Relativo Médio (MAPE): {mape:.2f}%")

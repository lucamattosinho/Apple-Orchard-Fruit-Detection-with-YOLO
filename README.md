# 🍏 Apple Orchard Fruit Detection with YOLO  

## 📌 About the Project  
This project leverages **computer vision** to detect and count apples in orchards using deep learning techniques with **YOLOv8 and YOLO11**. The goal is to demonstrate how **convolutional neural networks (CNNs)** can be applied to **agriculture automation**, optimizing crop monitoring and improving harvest efficiency.  

🔍 **Key challenges addressed:**  
- Fruit overlap and lighting variations  
- Image annotation and dataset preparation
- Hyperparameter tuning for improved performance  

📊 **Key results:**  
✅ **Model precision**: 92% (training) / 89% (testing)  
✅ **F1-Score**: 89.3% (training) / 87% (testing)  
✅ **mAP@50**: 93.9% (training) / 91% (testing)  

---

## 🛠️ Technologies Used  
- **Language**: Python  
- **Frameworks**: PyTorch, Ultralytics YOLO  
- **Libraries**: OpenCV, NumPy, Pandas  
- **Annotation Tools**: LabelImg  
- **Hardware**: NVIDIA RTX 4060  

---

## 📂 Project Structure  
```
📁 models/                   # Trained models and weights  
📁 prep_scripts/                  # Preprocessing and inference scripts  
📁 results/                  # Detection results on images and videos  
📜 README.md                 # This document  
```

---

## 📊 Results  
The models were tested on a real-world dataset, achieving **89% precision** and an **F1-Score of 87%**. Below are some detection examples:  

📷 **Predictions on images:**  
![Results](results/example_predictions.png)  

🎥 **Predictions on videos:**  
[Watch here](https://github.com/lucamattosinho/TCC/videos)  

---

## 💡 Real-World Applications  
🌱 Precision agriculture  
📸 Crop monitoring  
🤖 Agricultural automation  

This project can be expanded to detect other types of fruits, optimize the model for embedded devices, and integrate with drones for orchard mapping.  

📫 **Contact:** [Your LinkedIn or email]  

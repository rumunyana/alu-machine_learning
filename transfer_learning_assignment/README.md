## Weather Prediction

# Description

The goal of this project is to significantly enhance the capabilities of an existing weather application through the integration of satellite imagery. By applying transfer learning techniques with pretrained models, we aim to predict severe weather conditions more accurately and reliably. This project uses a dataset of satellite images that depict various weather conditions, processed and augmented to train models efficiently.

# Dataset

The dataset comprises satellite images categorized by different atmospheric phenomena. The images undergo several preprocessing and augmentation steps, including resizing, normalization, and data augmentation techniques such as rotation, horizontal and vertical flipping, and scaling, to improve the robustness of the models.

# Pre-trained Models

In this project, we leverage the following pre-trained models, chosen for their proven effectiveness and suitability for image-based tasks:

InceptionV3: Known for its ability to detect features at multiple scales, making it ideal for detailed satellite images.
ResNet50: Utilizes deep residual learning to allow for very deep networks, which are effective for complex image classification tasks.
EfficientNet: Offers scalability and efficiency, which is crucial for handling large sets of high-resolution images.

# Evaluation Metrics

To assess the performance of the fine-tuned models, we use the following evaluation metrics:

Accuracy: Measures the proportion of correctly predicted instances out of the total instances.
Precision, Recall, and F1 Score: These metrics help in understanding the model's effectiveness in predicting severe weather accurately.

# Experiment Results

The table below summarizes the performance of the fine-tuned models, providing a clear comparison based on accuracy and other significant metrics:

Model	    Accuracy	Precision	Recall	F1 Score
InceptionV3	 TBD	       TBD	     TBD	TBD
ResNet50	 TBD	       TBD	     TBD	TBD
EfficientNet TBD	       TBD	     TBD	TBD

## Findings

# Strengths:

Transfer Learning: Leveraging pre-trained models reduces both training time and computational resources while maintaining high accuracy.
Data Augmentation: Enhances the generalization of models, thereby improving their performance across various unseen weather conditions.

# Limitations:

Fixed Feature Extraction: Some specific atmospheric features may not be fully captured due to the general nature of pre-trained models.
Dataset Diversity: The performance of the models might be limited by the size and diversity of the training dataset.

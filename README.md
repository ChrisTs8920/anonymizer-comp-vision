# Anonymization - Blurring of license plates and human faces with Python and OpenCV

## Description

This project uses Python and OpenCV to detect and blur license plates and human faces in input images.

Techniques used:

- **Gaussian blur** (for object blurring)
- **Haar cascades** (for object detection)

>Images provided by: [Pexels](https://www.pexels.com/)

>*This project was made during my Computer vision course in university.*

## Summary

The anonymization of license plates and human faces is a critical task required in various fields such as surveillance, autonomous driving and public data sharing. Anonymization ensures privacy while preserving the usefulness of the data.

### Gaussian blur

Gaussian blur (or Gaussian smoothing) is the result of blurring an image using a gaussian function. It was named after mathematician and scientist Carl Friedrich Gauss and is used mainly used to reduce noise in an image but also to reduce detail (blurring).

### Haar cascades

Developed by Paul Viola and Michael Jones, it's a machine learning technique that identifies objects in an image. A Haar classifier uses Haar like features (digital image features used in object recognition) for object detection and it's trained using a large set of positive (that contain the object) and negative (without the object) images. The training process involves selecting the most efficient Haar like features and combining them to create a strong classifier. Feature selection is done using algorithms such as AdaBoost. Haar classifiers were used in the first real-time face detector.

>[Video demonstration of Haar cascades in action.](https://www.youtube.com/watch?v=hPCTwxF0qf4)

## A note on accuracy and performance

Limitations of Haar cascades include:

- **Detection accuracy:** The algorithm has mostly good results but produces many **false positives**. This lowers the algorithm's accuracy. Accuracy can be increased by tweaking the algorithm parameters.
- **Real-time processing:** Execution time is relatively high for real-time use. Execution time is affected by image resolution and algorithm parameters.

>**Deep learning based detection techniques like YOLO (You Only Look Once) and SSD (Single Shot multibox Detector) offer greater performance - high speed and accuracy.**

## Usage

1. Place images inside the ```input_images``` directory
2. Execute python script
3. Output images will be saved inside ```output_images``` directory

## Example results

### Example 1

|![Example 1](https://github.com/ChrisTs8920/anonymizer-comp-vision/blob/main/input_images/img1.jpg?raw=true)|![Example 1 blurred](https://github.com/ChrisTs8920/anonymizer-comp-vision/blob/main/output_images/output_img1.jpg?raw=true)|
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

### Example 2

|![Example 2](https://github.com/ChrisTs8920/anonymizer-comp-vision/blob/main/input_images/img2.jpeg?raw=true)|![Example 2 blurred](https://github.com/ChrisTs8920/anonymizer-comp-vision/blob/main/output_images/output_img2.jpeg?raw=true)|
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

### Example 3

|![Example 3](https://github.com/ChrisTs8920/anonymizer-comp-vision/blob/main/input_images/img3.jpg?raw=true)|![Example 3 blurred](https://github.com/ChrisTs8920/anonymizer-comp-vision/blob/main/output_images/output_img3.jpg?raw=true)|
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

[!alt text](./images/CTiX-CT-TSA.jpg)
# MISK Data Science Program

# Overview
Airport security sand safety may refer to the detection of unsafe object and materials passenger's baggage. The detection of threat object using X-ray luggage scan images is big part of avitation security.

# Dataset

The dataset was obtained from this [github](https://github.com/bywang2018/security-dataset). The data contains total of 47677 xray scan, and total of 12 categories of prohibited items that includ gun, knife, wrench, pliers, scissors, hammer, handcuffs, baton, sprayer, powerbank, lighter, bullet. 

The data is splitted into ~60% train set, and ~40% test sets. Also, the test sit is splited into the diffculity degree of detection:

1. Easy (~20%): One prohibited item in the scan.
2. Hard (~8%): More than 1 prohibited item in the scan.
3. Hidden (~10%): The prohibited item is hidden deliberetely.

# Models Used
- [YOLOv5](https://github.com/ultralytics/yolov5) was used to make object detection model 12 different prohibited items. 

# How to Use the trained model.
1. Clone this repo.
```bash
git clone https://github.com/ibrahim-g7/Baggage-Threat-Detection
```
2. Enter yolov5 folder.
```bash
cd yolov5
```
3. Put your input images in test_infer

4. Then run thw following command.
```bash
python detect.py --weight runs/train/baggage_screening/weights/best.pt --img 640 --conf 0.4 --source ./test_infer
```
5. The output will be in the following directory 
```bash
yolov5/runs/train/detect/exp/
```
6 If you run the command multiple times, it will make new folder with name exp1, exp2, etc.
# Referances
1. [YOLO paper](https://arxiv.org/pdf/1506.02640.pdf)
2. [Dataset paper](https://arxiv.org/pdf/2108.07020.pdf )
3. [About mAP](https://jonathan-hui.medium.com/map-mean-average-precision-for-object-detection-45c121a31173 )
4. [Object detection metric](https://github.com/rafaelpadilla/Object-Detection-Metrics)
5. [YOLOv5 github](https://github.com/ultralytics/yolov5 )

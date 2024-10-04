import os
import pickle

import cv2

cap= cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

imgBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
# print(len(imgModeList))

# Load the encoding file
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode File Loaded")

modeType = 2
counter = 0
id = -1
imgStudent = []

while True:
    success, frame = cap.read()

    imgBackground[162:162 + 480, 55:55 + 640] = frame
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    # cv2.imshow('Webcam',frame)
    cv2.imshow('Face Attendance', imgBackground)
    cv2.waitKey(1)


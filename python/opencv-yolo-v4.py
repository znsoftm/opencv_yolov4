import cv2 as cv
import os
import time
import numpy as np 
os.getcwd()

WORKDIR=os.path.dirname(__file__)
LABELFILE=WORKDIR+os.sep+".."+os.sep+"data"+os.sep+"objdetect.names"
CFGFILE=WORKDIR+os.sep+".."+os.sep+"data"+os.sep+"objdetect.cfg"
WEIGHTFILE=WORKDIR+os.sep+".."+os.sep+"data"+os.sep+"objdetect.pattern"

IMGFILE=WORKDIR+os.sep+".."+os.sep+"images"+os.sep+"file.jpg"






net = cv.dnn_DetectionModel(CFGFILE, WEIGHTFILE)
net.setInputSize(608, 608)
net.setInputScale(1.0 / 255)
net.setInputSwapRB(True)

frame = cv.imread(IMGFILE)

with open(LABELFILE, 'rt') as f:
	names = f.read().rstrip('\n').split('\n')
print(names)
startTime = time.time()
classes, confidences, boxes = net.detect(frame, confThreshold=0.1, nmsThreshold=0.4)
endTime = time.time()
print("Time: {}s".format(endTime-startTime))

if(len(boxes) >0):

    for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
        label = '%.2f' % confidence
        label = '%s: %s' % (names[classId], label)
        labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        left, top, width, height = box
        top = max(top, labelSize[1])
        cv.rectangle(frame, box, color=(0, 255, 0), thickness=3)
        cv.rectangle(frame, (left, top - labelSize[1]), (left + labelSize[0], top + baseLine), (255, 255, 255), cv.FILLED)
        cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv.imshow('out', frame)
    cv.waitKey(0)

else:
    print("Not found!")









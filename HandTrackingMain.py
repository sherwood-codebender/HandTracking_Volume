# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 21:08:53 2021

@author: Sherwood
"""

import cv2
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)

detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHand(img)
    lmList = detector.findPosition(img)
    
    if len(lmList) != 0:
        print(lmList[8])
        
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
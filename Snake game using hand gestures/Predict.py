import numpy as np
from keras.models import load_model
import operator
import cv2
import sys, os
import pyautogui

model = load_model(r"C:\Users\surya\Desktop\Snake\Hand_Rec_New_grayscale.h5")

cap = cv2.VideoCapture(0)


while True:
    _, frame=cap.read()
    frame = cv2.flip(frame,1)
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[0])

    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)

    roi = frame[y1:y2, x1:x2]

    roi = cv2.resize(roi, (64, 64))

    thresholded = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    #thresholded = cv2.GaussianBlur(thresholded, (7, 7), 0)
    #test_image = thresholded

    _, test_image = cv2.threshold(thresholded, 120, 255, cv2.THRESH_BINARY)

    #frame = cv2.resize(frame,(256,256))
    #_, test_image = cv2.threshold(frame,120,255,cv2.THRESH_BINARY)

    cv2.imshow("test",test_image)
    result=model.predict(test_image.reshape(1,64,64,1))
    prediction = {'Right': result[0][0],
                  'Up': result[0][1],
                  'Down': result[0][2],
                  'Left': result[0][3],
                  }
    # Sorting based on top prediction
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)

    # Displaying the predictions
    cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    #cv2.putText(frame, "None",(10,120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.imshow("Frame", frame)

    ans = prediction[0][0]
    if ans == "Down":
        pyautogui.press("down")
        print("Down")
    elif ans == "Left":
        pyautogui.press("left")
        print("Left")
    elif ans == "Right":
        pyautogui.press("right")
        print("Right")
    else:
        pyautogui.press("up")
        print("up")


    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # esc key
        break


cap.release()
cv2.destroyAllWindows()
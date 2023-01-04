import cv2
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("/Users/mairuizhang/PycharmProjects/pythonProject/video/purePU.mov")
c = 1
timeRate = 5

while (True):
    ret, frame = cap.read()
    FPS = cap.get(5)
    if ret:
        frameRate = int(FPS) * timeRate
        if c % frameRate == 0:
            tim = c/int(FPS)
            print("time:" + str(tim) + "s")
            cropped1 = frame[240:300, 80:200]
            # cropped2 = frame[170:200, 55:100]
            im_pil1 = Image.fromarray(cv2.cvtColor(cropped1, cv2.COLOR_BGR2RGB))
            temp1 = pytesseract.image_to_string(im_pil1, lang="eng")
            # im_pil2 = Image.fromarray(cv2.cvtColor(cropped2, cv2.COLOR_BGR2RGB))
            # temp2 = pytesseract.image_to_string(im_pil2, lang="eng")
            f = open("purePU.txt","a")
            f.write(str(tim) + "   " + temp1 +"\n")

            # arry1.append(pytesseract.image_to_string(im_pil1, lang="eng"))
            # arry2.append(pytesseract.image_to_string(im_pil2, lang="eng"))
            print(pytesseract.image_to_string(im_pil1, lang="eng"))
            # print(pytesseract.image_to_string(im_pil2, lang="eng"))
        c += 1
        cv2.waitKey(1)
    else:
        print("finish")
        break

cap.release()

## 1 read frame with frame num

## 2 manipulate image to get specific image part with info for the num

## 3 read num for the given part

## 4 write data to file (csv, txt)

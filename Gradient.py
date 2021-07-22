import cv2

import numpy as np
from cv2 import imshow, waitKey, destroyAllWindows, namedWindow, imwrite, VideoCapture
from PIL import ImageTk, Image
import image
cam = VideoCapture(0)

img_counter = int(0)
"""while True:
    ret, frame = cam.read()
    imshow("test", frame)
    if not ret:
        break
    k = waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "img1.jpg".format(img_counter)
        imwrite(img_name, frame)
        print("{} written!".format(img_name))
        break
        img_counter += 1

cam.release()

destroyAllWindows()
"""
white = [0, 0 ,0]
black = [255, 255 ,255]

img = cv2.imread("C:/Users/Prayag/Desktop/Acad/SIH2020/SkyRegionDet/img1.jpg")
# cv2.imshow("Original", img)
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY).astype(float)
#cv2.imshow("GreyScale Image", grey)
cv2.imwrite("C:/Users/Prayag/Desktop/Acad/SIH2020/SkyRegionDet/greyscale.png", grey)
edge_x = cv2.Sobel(grey,cv2.CV_64F,1,0,ksize=3)
cv2.imwrite("C:/Users/Prayag/Desktop/Acad/SIH2020/SkyRegionDet/Sobel_x.png", edge_x)
edge_y = cv2.Sobel(grey,cv2.CV_64F,0,1,ksize=3)
cv2.imwrite("C:/Users/Prayag/Desktop/Acad/SIH2020/SkyRegionDet/Sobel_y.png", edge_y)
edge = np.sqrt(edge_x**2 + edge_y**2)
cv2.imwrite("C:/Users/Prayag/Desktop/Acad/SIH2020/SkyRegionDet/Sobel_final.png", edge)

"""
img = edge

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)


cv2.imwrite("C:/Users/Prayag/PycharmProjects/SIH2020/negative.png", img)
"""

blur = cv2.blur(edge,(5,5))
cv2.imwrite("C:/Users/Prayag/Desktop/Acad/SIH2020/SkyRegionDet/blur.png", blur)
retval, threshold = cv2.threshold(blur, 12, 255, cv2.THRESH_BINARY)
cv2.imwrite("C:/Users/Prayag/Desktop/Acad/SIH2020/SkyRegionDet/threshold.png", threshold)
# cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

final = threshold
flag = 0

# for i in range(final.shape[1]):
#     for j in range(final.shape[0]):       
#         # if final[j,i] == 0 or flag == True:
#         #     flag = False
#         if final[j,i] == 0:
#             final[j,i] = 255
#         else:
#             final[j,i] = 0
   

for i in range(final.shape[1]):
    for j in range(final.shape[0]):       
        if final[j,i] == 255 and flag == 0:
             flag = 1
#              print("check")
#         print(flag)
        if flag == 1:
            final[j,i] = 255
        elif flag == 0:
            final[j,i] = 0
    flag = 0

cv2.imshow('final',final)
cv2.imwrite("C:/Users/Prayag/Desktop/Acad/SIH2020/SkyRegionDet/final.png", final)
cv2.waitKey(0)
cv2.destroyAllWindows()




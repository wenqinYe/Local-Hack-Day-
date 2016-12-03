#image overlay code
import sys
import cv2

s_img = cv2.imread("C:/Users/angus/Documents/GitHub/Local-Hack-Day-/steve.png",-1)
l_img = cv2.imread("C:/Users/angus/Documents/GitHub/Local-Hack-Day-/angoose.jpg",-1)
print s_img
s_img =cv2.resize(s_img,(20, 20))

x_offset=0
y_offset=0
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

cv2.waitKey(0)

height= 0
width = 0


cv2.imshow("", l_img)
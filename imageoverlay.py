#image overlay code
import sys
import cv2

s_img = cv2.imread("C:/Users/angus/Documents/GitHub/Local-Hack-Day-/steve.png",-1)
l_img = cv2.imread("C:/Users/angus/Documents/GitHub/Local-Hack-Day-/angoose.jpg",-1)
print s_img

x_offset=680
y_offset=120
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
cv2.imshow('img-windows', l_img)
r=100/s_img.shape[1]
dim=(100, int(s_img.shape[0]*r))
resized=cv2.resize(s_img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)

import numpy as np
import cv2

# Load an color image in grayscale
initial = 0
final = 78

for i in range(initial, final+1) :
    im_gray = cv2.imread(f'D:\SHASHANK\MAJOR-PROJECT\Datasets\sample\{i}.jpg',0)
    (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imwrite(f'D:\SHASHANK\MAJOR-PROJECT\Datasets\ppppp\{i}.jpg', im_bw)

print('done')
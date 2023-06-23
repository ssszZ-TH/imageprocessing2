import cv2 as cv
import numpy as np
import power_law

path_to_img = "./18558.jpg"
img = cv.imread(path_to_img,cv.IMREAD_GRAYSCALE)
img_h, img_w = img.shape
split_width = 500
split_height = 500


def start_points(size, split_size, overlap):
    points = [0]
    stride = int(split_size * (1-overlap))
    counter = 1
    while True:
        pt = stride * counter # หาตำเเหน่งที่ ploter จะเข้าไป plot 
        if pt + split_size >= size:
            if split_size == size:
                break
            points.append(size - split_size)
            break
        else:
            points.append(pt)
        counter += 1
    return points


X_points = start_points(img_w, split_width, 0.5)
Y_points = start_points(img_h, split_height, 0.5)

#count = 0 #เอาไว้ยัดในชื่อรูป เพราะชื่อรูปซ้ำกันไม่ได้
#name = 'splitted'
#frmt = 'png'

for i in Y_points:
    for j in X_points:
        split = img[i:i+split_height, j:j+split_width]
#         cv.imwrite('{}_{}.{}'.format(name, count, frmt), split)
#         count += 1
print(split.shape)
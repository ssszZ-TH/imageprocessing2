import cv2 as cv
import numpy as np
import power_law


histrogram_mean_val = 128
window_size = 100
gamma_val1 = 0.5 # มากกว่า 1 คือ ลดเเสง
gamma_val2 = 1.5 # น้อยกว่า 1 คือ เร่งเเสง

def split(img, window_size, margin): # เเบ่งภาพเป็นชิ้นๆ โดยภาพเกยกันตามระบะ margin

    sh = list(img.shape)
    sh[0], sh[1] = sh[0] + margin * 2, sh[1] + margin * 2
    img_ = np.zeros(shape=sh)
    img_[margin:-margin, margin:-margin] = img

    stride = window_size
    step = window_size + 2 * margin

    nrows, ncols = img.shape[0] // window_size, img.shape[1] // window_size
    splitted = []
    for i in range(nrows):
        for j in range(ncols):
            h_start = j*stride
            v_start = i*stride
            cropped = img_[v_start:v_start+step, h_start:h_start+step]
            splitted.append(cropped)
    return splitted

img_in = cv.imread("./18558.png",cv.IMREAD_GRAYSCALE)

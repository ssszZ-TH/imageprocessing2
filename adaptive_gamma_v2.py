import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



if __name__=="__main__":
    # setting
    path_to_img = "./dif_shade.jpeg"
    img = cv.imread(path_to_img,cv.IMREAD_GRAYSCALE)
    img = np.array(img, dtype="uint8")
    img_h, img_w = img.shape
    split_size = 500
    dark_zone = 128
    gamma_light_up = 0.2
    gamma_light_down = 1.8
    
    img = img[0:500,0:500]
    
    
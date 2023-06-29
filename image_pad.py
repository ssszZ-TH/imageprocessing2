import cv2 as cv
import numpy as np

def padding(img,r):
    reflect_img = cv.copyMakeBorder(img,r,r,r,r,cv.BORDER_REFLECT)
    return reflect_img

if __name__ == "__main__":
    img = cv.imread('dif_shade.jpeg')
    img = np.array(img, dtype="uint8")
    img = padding(img,300)
    cv.imwrite("./paded.png",img)
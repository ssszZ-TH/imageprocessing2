import cv2 as cv
import numpy as np

def power_law(part,gamma):
    img_in = cv.imread(part,cv.IMREAD_GRAYSCALE)

    gamma_corrected = (img_in / 255) ** gamma

    gamma_corrected = gamma_corrected*255

    img_out = np.array(gamma_corrected , dtype="uint8")

    cv.imshow("sitthipong" , img_out)

    cv.imwrite("demo1.png" , img_out)
    
if __name__  == "__main__":
    power_law("./18555.jpg",0.2)
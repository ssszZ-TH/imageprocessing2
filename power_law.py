import cv2 as cv
import numpy as np

def power_law(img_in,gamma): # ที่อยู่ไฟล์ gamma
    gamma_corrected = (img_in / 255) ** gamma
    gamma_corrected = gamma_corrected*255
    return np.array(gamma_corrected , dtype="uint8")

    
    
if __name__  == "__main__":
    part="./18558.jpg"
    img_in = cv.imread(part,cv.IMREAD_GRAYSCALE)
    img_out = power_law(img_in,0.2)
    cv.imwrite("demo1.png" , img_out)
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



if __name__=="__main__":
    # setting
    path_to_img = "./dif_shade.jpeg"
    img = cv.imread(path_to_img,cv.IMREAD_GRAYSCALE)
    img = np.array(img, dtype="uint8")
    split_size = 500
    dark_zone = 128
    gamma_light_up = 0.2
    gamma_light_down = 1.8
    
    
    ## img[0:500,0:500] #[y:y , x:x] 
    
    img_out = np.zeros(img.shape,dtype="uint8")
 
    for r in range(0, img.shape[0] ,split_size):
        for c in range(0, img.shape[1] ,split_size):
            cv.imshow("slice",img[r:r+split_size, c:c+split_size])
            cv.waitKey(0)
            cv.destroyAllWindows()
            
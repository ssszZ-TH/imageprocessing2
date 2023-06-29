import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from power_law import power_law
from image_pad import padding


if __name__=="__main__":
    # setting
    path_to_img = "./dif_shade.jpeg"
    img = cv.imread(path_to_img,cv.IMREAD_GRAYSCALE)
    img = np.array(img, dtype="uint8")
    split_size = 50
    overlap=25
    dark_zone = 2
    gamma_light_up = 0.5
    gamma_light_down = 1.5
    
    
    ## img[0:500,0:500] #[y:y , x:x] 
    
    img_out = np.zeros(img.shape,dtype="uint8")
 
    for r in range(0, img.shape[0] ,split_size):
        for c in range(0, img.shape[1] ,split_size):
            # cv.imshow("slice",img[r:r+split_size, c:c+split_size])
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            img_ = img[r:r+split_size, c:c+split_size]
            
            ##เเต่งรูปเล็กๆ เเต่ละรูป
            histrogram = cv.calcHist([padding(img_,overlap)],[0],None,[256],[128,256]) #padding นัดไปตรงๆ
            histrogram_mean = histrogram.mean()
            print(histrogram_mean)
            
            if histrogram_mean<=dark_zone:
                img_=power_law(img_,gamma_light_up)
            else :
                img_=power_law(img_,gamma_light_down)
            
            img_out[r:r+split_size, c:c+split_size] = img_
            
    cv.imwrite("./output.png",img_out)
    cv.imshow("spa_adaptive_light",img_out)
    cv.waitKey(0)
    cv.destroyAllWindows()
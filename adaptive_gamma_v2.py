import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



if __name__=="__main__":
    # setting
    path_to_img = "./dif_shade.jpeg"
    img = cv.imread(path_to_img,cv.IMREAD_GRAYSCALE)
    img = np.array(img, dtype="uint8")
    split_size = 250
    dark_zone = 128
    gamma_light_up = 0.2
    gamma_light_down = 1.8
    
    
    #img = img[0:500,0:500] #[y:y , x:x] 
    img_h, img_w = img.shape
    step_y = img_h//split_size
    step_x = img_w//split_size
    startx_=0
    starty_=0
    endx_=split_size
    endy_=split_size
    print("image size x,y =",img_w,img_h)
    print("step x y = ", step_x, step_y)
    for y in range(step_y):
        
        #กัน focus หลุดกรอบรูป
        if endy_>img_h:
            break
            
        for x in range(step_x):
            
            # กัน focus หลุดกรอบรุป
            if endx_>img_w:
                continue
            
            # เเบ่งรูป ตามเเนว [y ถึง y , x ถึง x]
            img_splited = img[starty_:endy_ , startx_:endx_]
            print("now focus on (x-x,y-y)=",startx_,endx_,"   ",starty_,endy_)
            
            #shift ตำเเหน่ง focusไปทาง x+
            startx_+=split_size
            endx_+=split_size
            
            #เเสดงรูป
            cv.imshow('graycsale image',img_splited)
            cv.waitKey(0)
            cv.destroyAllWindows()
            
        # shift y ไปทาง y+
        starty_+=split_size
        endy_+=split_size
        
        # shift x focus ให้กลับไปมองตรง ซ้ายสุดอีกรอบ
        startx_=0
        starty_=split_size
        
        print("ทำตรงนี้")
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path_to_img = "./dif_shade.jpeg"
img = cv.imread(path_to_img,cv.IMREAD_GRAYSCALE)
img = np.array(img, dtype="uint8")
img_h, img_w = img.shape
split_width = 500
split_height = 500
dark_zone = 128
gamma_light_up = 0.5
gamma_light_down = 1.5

def tune_light(img, light_up=True):
    pass
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

count = 0 #เอาไว้ยัดในชื่อรูป เพราะชื่อรูปซ้ำกันไม่ได้
name = 'splitted'
frmt = 'png'


for i in Y_points:
    for j in X_points:
        splited = img[i:i+split_height, j:j+split_width]
        histrogram = cv.calcHist([splited],[0],None,[256],[128,256])
        if histrogram.mean() <= dark_zone :
            print("up_light", end="\t\t")
        else :
            print("dn_light", end="\t\t")
        #cv.imwrite('{}_{}.{}'.format(name, count, frmt), split) ##debug ว่าภาพเเบ่งจริงอะป่าว
        #count += 1
        # plt.plot(histrogram)#debug ว่าทำไมค่า mean sum ออกมาเท่ากันทุกตัวเลย
        # plt.title('Histogram for gray scale image')
        # plt.show()
    print("\n")
        
#print(all_grayscale)

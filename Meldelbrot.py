
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def mendlebrot(Px,Py):
    max_iter = 100
    x=0
    y=0
    check =0


    for _ in range(max_iter):

        x_temp = x **2 - y **2
        y_temp = 2 * x * y
        x =x_temp + Px
        y = y_temp + Py
        check = abs(x +y)
        if check >10:
            return False
    return True

img = np.zeros([10000,10000,3],dtype=np.uint8)
x,y ,z= img.shape


for Py in range(y):
    for Px in range(x):
        New_x = np.interp(Px, [0, x], [-2, 2])
        New_y = np.interp(Py, [0, y], [-2, 2])

        if  mendlebrot(New_x,New_y):
            img.itemset((Py,Px,0),50)


im = Image.fromarray(np.uint8((img)*255))
im.save('test1.tiff', "TIFF")


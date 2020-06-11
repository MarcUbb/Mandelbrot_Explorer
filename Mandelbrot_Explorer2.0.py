import tkinter as T
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cmath
import random
import time

res = 100
pos_x = 0.0
pos_y = 0.0
zoom = 0.25
depth = 50
image = 0

def execute(RES,POS_X,POS_Y,ZOOM,DEPTH):
    random.seed(1320331)
    RES = RES
    DEPTH = DEPTH

    POS_X = POS_X
    POS_Y = POS_Y
    ZOOM = ZOOM

    start = time.time()
    global image
    image = np.full((RES,RES,3), (0),dtype=np.uint8)

    color_r = [40]
    color_g = [20]
    color_b = [60]

    i = 0
    while i < 255:
        color_r.append(color_r[i]+random.randint(-15,15))
        color_g.append(color_g[i]+random.randint(-15,15))
        color_b.append(color_b[i]+random.randint(-15,15))
        if color_r[i+1] > 255:
            color_r[i+1] = 255
        if color_g[i+1] > 255:
            color_g[i+1] = 255
        if color_b[i+1] > 255:
            color_b[i+1] = 255

        if color_r[i+1] < 0:
            color_r[i+1] = 0
        if color_g[i+1] < 0:
            color_g[i+1] = 0
        if color_b[i+1] < 0:
            color_b[i+1] = 0
        i += 1


    #print(color_r)
    #print(color_g)
    #print(color_b)

    def set(z):
        c = z
        i = 0
        while(i<DEPTH):
            i+=1
            z = z*z+c
            if(abs(z)>2):
                return i
        return 0


    i = 0
    while i < RES:
        j = 0
        while j < RES:
            z = int((set(complex((i*(1/ZOOM)/RES)-0.5*(1/ZOOM)+POS_X, (j*(1/ZOOM)/RES)-0.5*(1/ZOOM)+POS_Y))/DEPTH)*255)
            if z != 0:
                image[i,j,0]= color_r[z]
                image[i,j,1]= color_g[z]
                image[i,j,2]= color_b[z]
            j += 1
        i += 1
        print(i)

    end = time.time()
    print(end-start)

    plt.tight_layout()
    plt.imshow(image)
    plt.title("res = " + str(RES) + "  pos_x = " + str(POS_X) + "  pos_y = " + str(POS_Y) + "  zoom = " +  str(ZOOM) + "  depth = " + str(DEPTH))
    plt.show()
    

########################################################

def up():
    global pos_y
    pos_y = pos_y + 0.5/zoom
    
    execute(res, pos_x, pos_y, zoom, depth)
def left():
    global pos_x
    pos_x = pos_x - 0.5 / zoom
    execute(res, pos_x, pos_y, zoom, depth)

def right():
    global pos_x
    pos_x = pos_x + 0.5 / zoom
    execute(res, pos_x, pos_y, zoom, depth)
def down():
    global pos_y
    pos_y = pos_y - 0.5 / zoom
    execute(res, pos_x, pos_y, zoom, depth)


def zoom_in():
    global zoom
    zoom = zoom*2
    execute(res, pos_x, pos_y, zoom, depth)
def zoom_out():
    global zoom
    zoom = zoom/2
    execute(res, pos_x, pos_y, zoom, depth)

def change():
    global depth
    global res
    depth = d.get()
    res = r.get()
    execute(res, pos_x, pos_y, zoom, depth)

def save():
    im = Image.fromarray(image,"RGB")
    im.save("res = " + str(RES) + "  pos_x = " + str(POS_X) + "  pos_y = " + str(POS_Y) + "  zoom = " +  str(ZOOM) + "  depth = " + str(DEPTH) +".png")


########################################################


menu = T.Tk()
menu.title("Mandelbrot Explorer")
menu.geometry('300x200')

top_F = T.Frame(menu)
top_F.pack()
move_F = T.Frame(top_F)
move_F.pack(side = T.LEFT)
zoom_F = T.Frame(top_F)
zoom_F.pack(side = T.RIGHT)

bottom_F = T.Frame(menu)
bottom_F.pack()
depth_F = T.Frame(bottom_F)
depth_F.pack()
res_F = T.Frame(bottom_F)
res_F.pack()

########################################################

up_B = T.Button(move_F, text = "^", command = left)
up_B.pack(side = T.TOP)
left_B = T.Button(move_F, text = "<", command = down)
left_B.pack(side = T.LEFT)
right_B = T.Button(move_F, text = ">", command = up)
right_B.pack(side = T.RIGHT)
down_B = T.Button(move_F, text = "v", command = right)
down_B.pack(side = T.BOTTOM)

zoom_in_B = T.Button(zoom_F, text = "+", command = zoom_in)
zoom_in_B.pack(side = T.TOP)
zoom_out_B = T.Button(zoom_F, text = "-", command = zoom_out)
zoom_out_B.pack(side = T.BOTTOM)

depth_L = T.Label(depth_F, text = "depth")
d = T.IntVar()
depth_S = T.Scale(depth_F, variable = d, orient = T.HORIZONTAL, to = 2000)
depth_L.pack(side = T.LEFT)
depth_S.pack(side = T.RIGHT)

res_L = T.Label(res_F, text = "resolution")
r = T.IntVar()
res_S = T.Scale(res_F, variable = r, orient = T.HORIZONTAL, to = 10000)
res_L.pack(side = T.LEFT)
res_S.pack(side = T.RIGHT)

change_B = T.Button(bottom_F, text = "apply", command = change)
change_B.pack(side = T.BOTTOM)

save_B = T.Button(bottom_F, text = "save", command = save)
save_B.pack(side = T.RIGHT)

execute(res,pos_x,pos_y,zoom,depth)



menu.mainloop()
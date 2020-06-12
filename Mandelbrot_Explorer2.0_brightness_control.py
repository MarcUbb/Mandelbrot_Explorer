import tkinter as T
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cmath
import random
import time
import copy

res = 100
pos_x = 0.0
pos_y = 0.0
zoom = 0.25
depth = 50
image = 0

#######################################################################

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

color_r_copy = copy.deepcopy(color_r)
color_g_copy = copy.deepcopy(color_g)
color_b_copy = copy.deepcopy(color_b)

#######################################################################

def execute(RES,POS_X,POS_Y,ZOOM,DEPTH, color_r, color_g, color_b):
    random.seed(1320331)
    global image

    start = time.time()
    image = np.full((RES,RES,3), (0),dtype=np.uint8)

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

    #plt.tight_layout()
    plt.imshow(image)
    plt.title("res = " + str(RES) + "  pos_x = " + str(POS_X) + "  pos_y = " + str(POS_Y) + "  zoom = " +  str(ZOOM) + "  depth = " + str(DEPTH))
    plt.show()
    

########################################################

def up():
    global color_r
    global color_g
    global color_b
    global pos_y
    pos_y = pos_y + 0.5 / zoom
    
    execute(res, pos_x, pos_y, zoom, depth, color_r, color_g, color_b)
def left():
    global color_r
    global color_g
    global color_b
    global pos_x
    pos_x = pos_x - 0.5 / zoom
    execute(res, pos_x, pos_y, zoom, depth, color_r, color_g, color_b)

def right():
    global color_r
    global color_g
    global color_b
    global pos_x
    pos_x = pos_x + 0.5 / zoom
    execute(res, pos_x, pos_y, zoom, depth, color_r, color_g, color_b)
def down():
    global color_r
    global color_g
    global color_b
    global pos_y
    pos_y = pos_y - 0.5 / zoom
    execute(res, pos_x, pos_y, zoom, depth, color_r, color_g, color_b)


def zoom_in():
    global color_r
    global color_g
    global color_b
    global zoom
    zoom = zoom*2
    execute(res, pos_x, pos_y, zoom, depth, color_r, color_g, color_b)
def zoom_out():
    global color_r
    global color_g
    global color_b
    global zoom
    zoom = zoom/2
    execute(res, pos_x, pos_y, zoom, depth, color_r, color_g, color_b)

def change():
    global depth
    global res
    global brightness

    global color_r_copy
    global color_g_copy
    global color_b_copy

    global color_r
    global color_g
    global color_b

    depth = d.get()
    res = r.get()
    brightness = b.get()

    i = 0
    j = 256-brightness
    while i < 255:
        color_r[i] = color_r_copy[i]
        color_g[i] = color_g_copy[i]
        color_b[i] = color_b_copy[i]
        i += 1
    i = 0
    while i < j:
        color_r[i] = color_r_copy[i]/j
        color_g[i] = color_g_copy[i]/j
        color_b[i] = color_b_copy[i]/j
        print(j)
        i += 1
        j -= 1
    execute(res, pos_x, pos_y, zoom, depth, color_r, color_g, color_b)

def save():
    im = Image.fromarray(image,"RGB")
    im.save("res = " + str(res) + "  pos_x = " + str(pos_x) + "  pos_y = " + str(pos_y) + "  zoom = " +  str(zoom) + "  depth = " + str(depth) +".png")


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
res_L.pack(side = T.RIGHT)
res_S.pack(side = T.RIGHT)

brightness_L = T.Label(res_F, text = "brightness")
b = T.IntVar()
brightness_S = T.Scale(res_F, variable = b, orient = T.HORIZONTAL, to = 255)
brightness_L.pack(side = T.LEFT)
brightness_S.pack(side = T.LEFT)

change_B = T.Button(bottom_F, text = "apply", command = change)
change_B.pack(side = T.BOTTOM)

save_B = T.Button(bottom_F, text = "save", command = save)
save_B.pack(side = T.RIGHT)

execute(res,pos_x,pos_y,zoom,depth, color_r, color_g, color_b)



menu.mainloop()
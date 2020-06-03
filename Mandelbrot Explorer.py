import Tkinter as T
import tkMessageBox
import matplotlib.pyplot as plt
import cmath
import random
import time

res = 200
pos_x = 0.0
pos_y = 0.0
zoom = 0.25
depth = 50

def execute(res,pos_x,pos_y,zoom,depth):
    start = time.time()

    x = [[] for _ in range(0, depth + 1)]
    y = [[] for _ in range(0, depth + 1)]

    def set(z):
        c = z
        i = 0
        while (i < depth):
            z = z * z + c
            if (abs(z) > 2):
                return depth - i
            i += 1
        return 0

    i = 0
    c = 0.0
    while (i < res):
        j = 0
        while (j < res):
            z = complex((i * (1 / zoom) / res) - 0.5 * (1 / zoom) + pos_x,
                        (j * (1 / zoom) / res) - 0.5 * (1 / zoom) + pos_y)
            x[set(z)].append(z.real)
            y[set(z)].append(z.imag)
            j += 1

        per = round(75 * (c + 1) / res, 1)
        if(per - round(per) == 0):
            print per, "%"
        i += 1
        c += 1

########################################################

    def color(n):
        if (n == 0):
            color = list('#000000')
            colorcode = "".join(color)
            return colorcode

        else:
            n = 15728639 * random.randint(1, depth) / depth
            n += 1048576
            n = hex(n)
            color = list(str('#' + n))

            del (color[1], color[1])
            if (len(color) > 7):
                del (color[7])
            colorcode = "".join(color)
            return colorcode

    k = 0
    c = 0.0

    plt.clf()
    while (k < depth):
        colour = color(k)
        plt.scatter(x[k], y[k], s=0.25, c=colour)
        per = round(75 + 25 * (c + 1) / depth, 1)
        if (per - round(per) == 0):
            print per, "%"
        k += 1
        c += 1

########################################################

    end = time.time()
    print end - start, "s"

    plt.title("res = " + str(res) + "  pos_x = " + str(pos_x) + "  pos_y = " + str(pos_y) + "  zoom = " +  str(zoom) + "  depth = " + str(depth))
    plt.show()

########################################################

def up():
    global pos_y
    pos_y = pos_y + 0.5/zoom
    print "est. time:", (float(depth) / 100.0) * (float(res) / 100.0) ** 2 / 10, "s"
    execute(res, pos_x, pos_y, zoom, depth)
def left():
    global pos_x
    pos_x = pos_x - 0.5 / zoom
    print "est. time:", (float(depth) / 100.0) * (float(res) / 100.0) ** 2 / 10, "s"
    execute(res, pos_x, pos_y, zoom, depth)

def right():
    global pos_x
    pos_x = pos_x + 0.5 / zoom
    print "est. time:", (float(depth) / 100.0) * (float(res) / 100.0) ** 2 / 10, "s"
    execute(res, pos_x, pos_y, zoom, depth)
def down():
    global pos_y
    pos_y = pos_y - 0.5 / zoom
    print "est. time:", (float(depth) / 100.0) * (float(res) / 100.0) ** 2 / 10, "s"
    execute(res, pos_x, pos_y, zoom, depth)


def zoom_in():
    global zoom
    zoom = zoom*2
    print "est. time:", (float(depth) / 100.0) * (float(res) / 100.0) ** 2 / 10, "s"
    execute(res, pos_x, pos_y, zoom, depth)
def zoom_out():
    global zoom
    zoom = zoom/2
    print "est. time:", (float(depth) / 100.0) * (float(res) / 100.0) ** 2 / 10, "s"
    execute(res, pos_x, pos_y, zoom, depth)

def change():
    global depth
    global res
    depth = d.get()
    res = r.get()
    print "est. time:", (float(depth) / 100.0) * (float(res) / 100.0) ** 2 / 10, "s"
    execute(res, pos_x, pos_y, zoom, depth)

########################################################


menu = T.Tk()
menu.title("Mandelbrot Explorer")

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

up_B = T.Button(move_F, text = "^", command = up)
up_B.pack(side = T.TOP)
left_B = T.Button(move_F, text = "<", command = left)
left_B.pack(side = T.LEFT)
right_B = T.Button(move_F, text = ">", command = right)
right_B.pack(side = T.RIGHT)
down_B = T.Button(move_F, text = "v", command = down)
down_B.pack(side = T.BOTTOM)

zoom_in_B = T.Button(zoom_F, text = "+", command = zoom_in)
zoom_in_B.pack(side = T.TOP)
zoom_out_B = T.Button(zoom_F, text = "-", command = zoom_out)
zoom_out_B.pack(side = T.BOTTOM)

depth_L = T.Label(depth_F, text = "depth")
d = T.IntVar()
depth_S = T.Scale(depth_F, variable = d, orient = T.HORIZONTAL, to = 1000)
depth_L.pack(side = T.LEFT)
depth_S.pack(side = T.RIGHT)

res_L = T.Label(res_F, text = "resolution")
r = T.IntVar()
res_S = T.Scale(res_F, variable = r, orient = T.HORIZONTAL, to = 2000)
res_L.pack(side = T.LEFT)
res_S.pack(side = T.RIGHT)

change_B = T.Button(bottom_F, text = "apply", command = change)
change_B.pack(side = T.BOTTOM)

print "est. time:", (float(depth)/100.0)*(float(res)/100.0)**2/10, "s"
execute(res,pos_x,pos_y,zoom,depth)



menu.mainloop()
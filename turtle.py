from turtle import *
import colorsys
speed(0)
pensize(2)
h = 0.5
bgcolor("Black")

for    i    in    range(160):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.004
    for    j    in    range(4):
        fd(i)
        rt(20)
        rt(60)
    rt(120)
    
done()
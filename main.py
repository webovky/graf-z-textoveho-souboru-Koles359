#!/usr/bin/env python3


import pylab
x = []
y = []
with open("soubor.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        x.append(float(line[0:15].strip()))
        y.append(float(line[17:35].strip()))


pylab.plot(x,y)
pylab.show()
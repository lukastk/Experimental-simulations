# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:44:26 2015

@author: Lukas
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 16:44:53 2014

@author: Lukas
"""

import numpy as np
from visual import sphere, vector, color, rate, display, label, box, curve

display(center=(0, 0, 0), width=800, height=600, autoscale=False)

offset = 1

factor = 5

ramp1 = box(pos=vector(-1 - offset, 0, 0)*factor, size=vector(1*factor, 0.05*factor, 1*factor), color=(0.5, 0.5, 0.5))
ramp2 = box(pos=vector(1 - offset, 0, 0)*factor, size=vector(1*factor, 0.05*factor, 1*factor), color=(0.5, 0.5, 0.5))
ramp3 = box(pos=vector(0 - offset, 0, 0)*factor, size=vector(1*factor, 0.05*factor, 0.2*factor), color=(0.5, 0.5, 0.5))

ball1 = sphere(pos=(0 - offset*factor, 0, 0),radius=0.4*factor,color=(1, 0, 0) ,make_trail=False)

ramp1 = box(pos=vector(-1 + offset, 0, 0)*factor, size=vector(1, 0.05, 1)*factor, color=(0.5, 0.5, 0.5))
ramp2 = box(pos=vector(1 + offset, 0, 0)*factor, size=vector(1, 0.05, 1)*factor, color=(0.5, 0.5, 0.5))
ramp3 = box(pos=vector(0 + offset, 0, 0)*factor, size=vector(1, 0.05, 0.2)*factor, color=(0.5, 0.5, 0.5))

ball2 = sphere(pos=(0 + offset*factor, 0, 0),radius=0.4*factor,color=(1, 0, 0) ,make_trail=False)

P = 102812.9266
A = 0.007975*0.007975*np.pi
V = 0.001148
gamma = 1.3

displacement = 0.1

ball1.y = -displacement
ball1.v = 0
ball1.F = -9.82
ball1.m = 0.0167
ball1.c = -P*A*A/V*gamma/ball1.m

ball2.y = -displacement
ball2.v = 0
ball2.m = ball1.m
ball2.c = ball1.c

dt = 0.0001
t = 0

rt = 2000

while True:
    a = 0
    if ball1.y > 0:
        a = ball1.F/ball1.m
    else:
        a = ball1.F/ball1.m + ball1.c*ball1.y
    
    ball1.v += a*dt
    ball1.y += ball1.v*dt
    
    a = ball2.c*ball2.y
        
    ball2.v += a*dt
    ball2.y += ball2.v*dt
        
    rate(rt)
    t += dt
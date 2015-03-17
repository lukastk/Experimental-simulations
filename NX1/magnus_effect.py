# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 00:58:23 2014

@author: Lukas
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 16:44:53 2014

@author: Lukas
"""

from visual import sphere, vector, color, rate, display, label, box, curve

class Ball:
    g = -400 # Graviation constant
    
    def __init__(self, m, pos, vel, ang_vel, color, rad, trail = False):
        """ Initiate instance"""
        self.b = sphere(pos=pos,radius=rad,color=color,make_trail=trail)
        self.vel = vel
        self.dv = vector(0,0,0)
        self.ang_vel = ang_vel
        self.dang_vel = vector(0,0,0)
        self.m = float(m)
        self.r = float(rad)
        self.stationary = False
        self.gravity = False
        self.collision = True
    
    def update(self, ball_list, dt):
        if self.stationary:
            return
        
        if self.collision:
            self.collision_check(ball_list)
        
        if self.gravity:
            self.dv.y += Ball.g*dt
        
        if self.gravity and magnus_effect:
            self.dv += (S/self.m)*(vector.cross(self.ang_vel, -self.vel))*dt
        
        self.vel += self.dv
        self.ang_vel += self.dang_vel
        # Calculate change in position
        self.b.pos += self.vel*dt
        
        if self.b.pos.y<(-h+ self.r):
            self.b.pos.y = (-h+ self.r)
            self.stationary = True
            return
            
        self.dv = vector(0, 0, 0)
        self.dang_vel = vector(0, 0, 0)
    
    def collision_check(self, ball_list):
        for b in ball_list:
            dist = self.b.pos - b.b.pos
            dist_mag = dist.mag
            
            if dist_mag <= self.r + b.r:
                self.collide(b)
                
    def collide(self, b):
        #Find axis of impulse
        e_par = (self.b.pos - b.b.pos).norm()
        
        if friction:
            self.dang_vel = -vector.cross(b.vel.norm(),e_par)*friction_ang_impulse
            b.dang_vel = vector.cross(b.vel.norm(),e_par)*friction_ang_impulse        
        
        u1 = vector.dot(self.vel, e_par)
        u2 = vector.dot(b.vel, e_par)
        
        """
        v1 = (u1 + (b.m/self.m)*(2*u2 - u1))/(1 + b.m/self.m)
        v2 = v1 + u1 - u2
        """
        
        v1 = (1/(1 + (b.m/self.m))) * (u1 + (b.m/self.m)*(u2 - e*(u1-u2)))
        v2 = v1 + e*(u1 - u2)
        
        self.vel = self.vel - vector.dot(self.vel, e_par)*e_par + v1*e_par
        b.vel = b.vel - vector.dot(b.vel, e_par)*e_par + v2*e_par
        
        self.gravity = True
        b.gravity = True   
        self.collision = False
        b.collision = False
        
        if ball_trail:
            self.b.make_trail = True
            b.b.make_trail = True
        
        if infintesimal:
            self.b.pos = vector(0, 0, 0)
            b.b.pos = vector(0, 0, 0)
            
ball_trail = True

magnus_effect = True
S = 0.5 # Air resistance coefficient

friction = True
friction_ang_impulse = 27

infintesimal = False

dt = 0.0001 # Time step
rt = 2000

h = 2.5
w = 30
l = 22.

e = 1

color_of_setup = (0.5,0.5,0.5)
edge_of_ramp = 0 #X-axis of edge of ramp
   
ball_list = []
    
ballrad = 0.5

display(center=(l/2, -h, 0), width=800, height=600)

ramp = box(pos=vector(-2 + edge_of_ramp-0.05-ballrad/2,-0.1,0), size=vector(4-ballrad, 0.1, ballrad), color=color_of_setup)
#wall = box(pos=vector(edge_of_ramp - 0.05,-float(h)/2 - 0.05,0), size=vector(0.1, h, w), color=color_of_setup)
platform = box(pos=vector(edge_of_ramp + l/2, -h-0.1, 0), size=vector(l, 0.1, w), color=color_of_setup)

b1 = None

simulation_end = False

angular_vel_step = 2
angular_vel_max = 20
angular_vel = -angular_vel_max

while True:
    if b1 == None or b1.stationary and not simulation_end:
        if b1 != None:
            ball_list.remove(b1)
        
        b1 = Ball(m = 1, pos=vector(-10, ballrad, 0), vel=vector(200, 0, 0), ang_vel = vector(0,angular_vel,0), color=color.red, rad=ballrad, trail=ball_trail)
        b1.gravity = True
        ball_list.append(b1)
        
        angular_vel += angular_vel_step
        
        if angular_vel >= angular_vel_max:
            simulation_end = True
    
    blist = ball_list[:]    
    
    while blist:
        b = blist.pop()
        b.update(blist, dt)
        
    # The rate of the program
    rate(rt)
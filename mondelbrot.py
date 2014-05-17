# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 07:58:52 2014

@author: cooper
"""

from pylab import imshow, show
import numpy as np
import math
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def __add__(self,num): 
        return Complex(self.r+num.r,self.i+num.i)
    
    def __mul__(self,num):
        return Complex(self.r*num.r - self.i*num.i, self.r*num.i + self.i*num.r)  
    
    def conj(self):
        return Complex(self.r,-self.i)
        
    def abs(self): 
        return np.sqrt(pow(self.r,2)+pow(self.i,2))
    
    def division(self,num):
        if pow(num.abs(),2)!=0:
            z_re = (self.r*num.r + self.i*num.i)/pow(num.abs(),2)
            z_im= (self.r*num.i - self.i*num.r)/pow(num.abs(),2)
        else: print 'Error: division by 0'    
        return (z_re,z_im)
    
    def printi(self):
        print self.r,' i',self.i

def mond_set(x, y, max_iters):
    c = Complex(x, y)
    z =Complex(0, 0)
    for i in range(max_iters):
        z = z*z + c
        if pow(z.abs(),2) >= 4:
            return i
    return max_iters

def fractal(x_min, x_max, y_min, y_max, image, iters):
    height = image.shape[0]
    width = image.shape[1]
    pixel_size_x = (x_max - x_min) / width
    pixel_size_y = (y_max - y_min) / height
    for x in range(width):
        real = y_min + x * pixel_size_x
        for y in range(height):
            imaginary = y_min+ y * pixel_size_y
            color = mond_set(real, imaginary, iters)
            image[y, x] = color
            
image = np.zeros((1024, 1024), dtype = np.uint8)
fractal(-2.0, 2.0, -2.0, 2.0, image, 20) 
imshow(image)
show()

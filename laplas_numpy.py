# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 11:23:58 2014

@author: cooper
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from numpy import *
n=1000
k=1000
l=1
x=linspace(0,l,num=k)
y=linspace(0,l,num=k)
x,y=meshgrid(x,y)
u=zeros((k,k))
for i in range(1,N,2):
    u=400*sin(pi*i*x/l)*sinh(pi*i*y/l)/(pi*i*sinh(pi*i))+u
fig = plt.figure()
ax = fig.gca(projection='3d')

s = ax.plot_surface(x,y,u, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)


ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

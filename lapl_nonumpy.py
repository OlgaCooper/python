# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 07:48:08 2014

@author: cooper
"""



import numpy as np

import matplotlib.cm as cm

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def fi(z):

 N=z.shape[0]

 m=[]

 for i in range(N):

  m.append([])

  for j in range(N):

   m[i].append(z[i,j])

 for n in range(100):

  for i in range(1,N-1):

   for j in range(1,N-1):

    m[i][j]=0.25*(m[i+0][j+1]+m[i+0][j-1]+m[i+1][j]+m[i-1][j])

 for i in range(N):

  for j in range(N):

   z[i,j]=m[i][j]

 return z


N=100

delta = 1./N

x = y = np.arange(0, 1., delta)

X, Y = np.meshgrid(x, y)

N=x.size

Z=np.zeros(X.size).reshape(N,N)


Z[0,0:]=100.



im = plt.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,

origin='lower', extent=[0,1.,0,1.],

vmax=abs(Z).max(), vmin=-abs(Z).max())

plt.title ("геодезическая")



fig = plt.figure()

ax = Axes3D(fig)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')


plt.show()
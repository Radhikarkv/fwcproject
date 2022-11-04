import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          
sys.path.insert(0,'/home/susi/Documents/CoordGeo')   

from line.funcs import *
from triangle.funcs import *
from conics.funcs import *
from math import *
import sympy as sym

import scipy.integrate as SInt
import subprocess
import shlex

#Standard ellipse
#lamda1=3
#lamda2=6
a = np.sqrt(6)
b = np.sqrt(3)
f=sym.Symbol('f')
λ1=-f/a**2 #semi major axes =a=sqrt((u^T*V^-1*U-f/)λ1)
λ2=-f/b**2 #semi minor axes =b=sqrt((u^T*V^-1*U-f/)λ2)
V0=np.array(([λ1,0],[0,λ2]))
V=V0/-f
V = np.array(([a,0],[0,b]))
#To find equation of ellipse
u=np.array([0,0])
x=sym.Symbol('x')
y=sym.Symbol('y')
X=np.array((x,y))
eq=(X.T@V@X)+2*(u.T@X)-1  #x^TVx + 2u^T x + f = 0
##Generating the ellipse
x_elli= ellipse_gen(a,b)
#v = ellipse_gen(a,b)
u=np.array([0,0])
x = np.linspace(0,10,100)
y = -x+7
plt.plot(x, y, '-r', label='y=-x+7')
q=np.array([2,1])
n=np.array(([1,1])) #normal vector
m=np.array([-1,1])
p=np.array([3,4])

#generating the line
x_qp=line_gen(q,p)

#Plotting the ellipse
plt.plot(x_elli[0,:],x_elli[1,:],label='$Ellipse$')

#Plotting the ellipse
#plt.plot(v[0,:],v[1,:],label='Standard Ellipse')

#Generating the tangent
#k1 = 2
#k2 = -2
#x_AB = line_dir_pt(m,q,k1,k2)
#Plotting all lines
#plt.plot(x_AB[0,:],x_AB[1,:],label='Tangent')
plt.plot(x_qp[0,:],x_qp[1,:],label='$line$')

#Labeling the coordinates
ellipse_coords = np.vstack((u,q,p)).T
plt.scatter(ellipse_coords[0,:], ellipse_coords[1,:])
vert_labels = ['u','q','p']
plt.axhline(y=0, c="yellow")
plt.axvline(x=0, c="yellow")
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (ellipse_coords[0,i], ellipse_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/home/susi/Documents/CoordGeo/ellipse.pdf')
#subprocess.run("termux-open  '/home/susi/Documents/CoordGeo/ellipse.pdf'")
#else
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/home/susi/Documents/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#Input parameters
r1=3
r2=1.5
o1=np.array([0,0])
o2=np.array([0.5,1.414])
p2=np.array([1,0])
##plt.plot(p2)
p=np.array([0,0])

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Generating the circle
x_circ = circ_gen(o1,r1)

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label="Circle1")

#Labelling the coordinates
tri_coords = np.vstack((o1,p2,o2)).T
print(tri_coords)
print("center of the inner circle is:",(0.5,1.414))
print("the radius of the inner circle is:",1.5)
plt.scatter(tri_coords[0,:], tri_coords[1,:])
#plt.scatter(cp1)
vert_labels = ['o1(0,0)','p2(1,0)','o2']
for i, txt in enumerate(vert_labels):
	plt.annotate(txt, #this is text
				 (tri_coords[0,i], tri_coords[1,i]), #this is the point to label
				textcoords="offset points" , # How to position the text
				xytext=(0,10),#Distance from the text to points (x,y)
				ha='center') # horizontal alignment can be left , right or center
#Generating points on a circle
def circ_gen_2(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Generating the circle
x_circ_2 = circ_gen_2(o2,r2)
x_o1p2 = line_gen(o1,p2)
plt.plot(x_o1p2[0,:],x_o1p2[1,:],label='$line$')

#Plotting the circle
plt.plot(x_circ_2[0,:],x_circ_2[1,:],label="Circle2")

				
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
#plt.show()
#if using termux
plt.savefig('/home/susi/Documents/figure1.pdf')
subprocess.run(shlex.split("termux-open '/home/susi/Documents/figure1.pdf'")) 
#else

				

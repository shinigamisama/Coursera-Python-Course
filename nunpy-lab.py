# import numpy library
import numpy as np 

# Create a python list

a = ["0", 1, "two", "3", 4]

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
print(a)

print(np.__version__)

# Check the type of the array

print(type(a))

# Check the type of the values stored in numpy array

print(a.dtype)

# Create numpy array

c = np.array([20, 1, 2, 3, 4])
print(c)

# Assign the first element to 100

c[0] = 100
print(c)

# Assign the 5th element to 0

c[4] = 0
print(c)

# Slicing the numpy array

d = c[1:4]
print(d)

# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
print(c)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

# Get the size of numpy array

print("size:",a.size)

# Get the number of dimensions of numpy array

print("dimension:",a.ndim)

# Get the shape/size of numpy array

print("shape:",a.shape)

u = np.array([1, 0])
u

v = np.array([0, 1])
v

# Numpy Array Addition

z = np.add(u, v)
z
# Plotting functions


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

Plotvec1(u, z, v)
  
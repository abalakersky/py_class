
""" ctrl + Shift + B will run the file. """

#Test Importing Numpy
import numpy as np

print("hello world")
#define a vector size 4
a = np.array([1, 2, 3, 4])
  
#define a 2x4 matrix
b = np.array([[ 1, 2, 3, 9], 
              [ 4, 5, 6, 9]]) 
 
print( a.dot(b.transpose()) ) 

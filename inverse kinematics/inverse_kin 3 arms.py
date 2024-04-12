from sympy import cos, sin, atan2
from sympy.matrices import Matrix
from numpy import pi

import matplotlib.pyplot as plt
import numpy as np
import math

l1 = 35
l2 = 30
l3 = 15

x = np.random.randint(0, 60) # l1+l2 < x < l1+l2+l3
y = np.random.randint(0, 60) 
z = 40

base_angle = math.atan2(z, x)

angles = [0, pi, pi/2]

def inv_kin():
  # parallel handling
  kx = x - l3 # l1*s1 + l2*s12
  ky = y      # l1*c1 + l2*c12

  c2 = (kx**2 + ky**2 - l1**2 - l2**2)/(2*l1*l2)
  s2 = np.sqrt(1-c2**2)
  theta_2 = float(atan2(s2, c2))

  M = Matrix([
    [l1+l2*c2, l2*s2],
    [-l2*s2  , l1+l2*c2]
  ])
  M_inv = M.inv()
  s1, c1 = M_inv*Matrix(2, 1, [kx, ky])
  theta_1 = float(atan2(s1, c1))

  theta_3 = pi/2 - theta_1 - theta_2

  angles = [theta_1, theta_2, theta_3]
  Plot((angles))

  return angles

   
def Plot(angles):
  a1, a2, a3 = angles
  plt.xlim((-50, 75))
  plt.ylim((-50, 75))
  
  xs = [0, l1*sin(a1), l1*sin(a1)+l2*sin(a1+a2), l1*sin(a1)+l2*sin(a1+a2)+l3*sin(a1+a2+a3)]
  ys = [0, l1*cos(a1), l1*cos(a1)+l2*cos(a1+a2), l1*cos(a1)+l2*cos(a1+a2)+l3*cos(a1+a2+a3)]

  plt.plot(xs, ys)
  plt.plot(x, y, 'ro')

  kx = x - l3 # l1*s1 + l2*s12
  ky = y      # l1*c1 + l2*c12
  plt.plot(kx, ky, 'ro')
  plt.plot(0, 0, 'ro')
  plt.show()

inv_kin()
from sympy import symbols, cos, sin, simplify, pprint, tan, expand_trig, sqrt, trigsimp, atan2
from sympy.matrices import Matrix
from numpy import pi

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time
import numpy as np
import math

# l1 = 35
# l2 = 30
# l3 = 15

# x = 30 
# y = 30
# z = 40
# phi = pi/4
# base_angle = math.atan2(z, x)

# angles = [0, pi, pi/2]

l1 = l2 = 3
x, y = 2, 0.5

def inv_kin():
  c2 = (x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2)
  s2 = np.sqrt(1-c2**2)
  theta_2 = float(atan2(s2, c2))

  M = Matrix([
    [l1+l2*c2, l2*s2],
    [-l2*s2  , l1+l2*c2]
  ])
  M_inv = M.inv()
  s1, c1 = M_inv*Matrix(2, 1, [x, y])
  theta_1 = float(atan2(s1, c1))

  # s1 = ((l1+l2*c2)*x - (l2*s2)*y)

  angles = [theta_1, theta_2]
  print(theta_1)

  Plot((theta_1, theta_2))
  print(s1, s2, c1, c2)

  return angles

def Plot(angles):
  a1, a2 = angles
  plt.xlim((-5, 5))
  plt.ylim((-5, 5))
  xs = [0, l1*sin(a1), l1*sin(a1)+l2*sin(a1+a2)]
  ys = [0, l1*cos(a1), l1*cos(a1)+l2*cos(a1+a2)]
  # print(ys)
  # ys = [0, l1*cos(a1), (l1+l2)*cos(a1+a2), (l1+l2+l3)*cos(a1+a2+a3)]
  # plt.plot(xs, ys)
  plt.plot(xs, ys)
  plt.plot(x, y, 'ro')
  plt.plot(0, 0, 'ro')
  plt.show()

# def Plot(s1, s2, c1, c2):
#   plt.xlim((-5, 5))
#   plt.ylim((-5, 5))
#   xs = [0, l1*s1, l1*s1+l2*(s1*c1+c1*s2)]
#   ys = [0, l1*c1, l1*c1+l2*(c1*c2-s1*s2)]

#   plt.plot(xs, ys)
#   # plt.plot(ys, xs)
#   plt.plot(x, y, 'ro')
#   plt.plot(0, 0, 'ro')
#   plt.show()

inv_kin()
# angs = [a*180/pi for a in inv_kin()]
# print(angs)
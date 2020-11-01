import lifegame2
import unittest
import pysnooper
import numpy as np
from numpy import *

m = (20, 20)
z = np.zeros(m)
l = np.ones(m)

c = np.zeros(8)
m0 = np.zeros(m)
m0[0][0] = 1
m0[0][19] = 1
m0[19][0] = 1
m0[19][19] = 1
print(m0)
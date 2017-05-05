import numpy as np
import pylab as plt
from collections import Iterable

class String_Wave:

	def __init__(self, N, m, k):
		self.N = N

		if isinstance(m, iterable):
			self.m = m
		else:
			self.m = np.array([m for i in range(N)])

		if isinstance(k, iterable):
			self.k = k
		else: 
			self.k = np.array([k for i in range(N)])


	def solver(self,dt,iterations,initvals):
		all_pos = []

		y_0 = initvals
		y_min = np.zeros(self.N)
		y_pluss = np.zeros(self.N)

		all_pos.append(y_0)

		for i in range(iterations):
			y_0,y_min,y_pluss = self.integrator(y_0,y_min,y_pluss)
			all_pos.append(y_pluss)

		return all_pos

	def integrator(self,y_0,y_min,y_pluss):
		
		

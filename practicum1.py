# -*- coding: utf-8 -*-

import random
import numpy

# Partial differentials

def partial_differential(i,a):
	if   a == "d/dx":
		for k1 in range(m-1):
			for k2 in range(n):
				i[k1][k2] = i[k1+1][k2] - i[k1][k2]
	elif a == "d/dy":
		for k1 in range(m):
			for k2 in range(n-1):
				i[k1][k2] = i[k1][k2+1] - i[k1][k2]
	elif a == "d^2/dx^2":
		for k1 in range(m-2):
                        for k2 in range(n):
                                i[k1][k2] = i[k1+2][k2] - 2 * i[k1+1][k2] + i[k1][k2]
	elif a == "d^2/dy^2":
		for k1 in range(m):
                        for k2 in range(n-2):
                                i[k1][k2] = i[k1][k2+2] - 2 * i[k1][k2+1] + i[k1][k2]
	else:
		print("incorrect input")

	return i


def convolution(i,kernel):
	tmp = []
	try:
		len(kernel[0])
	except IndexError:
		tmp = [-1]

	if tmp == [-1]:
		tmp = convolution_dimensional(i,kernel)
	else:
		tmp = convolution_two_dimensional(i,kernel)
	return tmp

def convolution_two_dimensional(i,kernel):
#                m   n
# (k*l)*[x,y] = SUM SUM k[i,j] * l[x-i,y-j]
#               j=1 i
	kernel_centerY = len(kernel) / 2
	kernel_centerX = len(kernel[0]) / 2
	sum = 0

	i2 = []
	for k1 in range(len(i)):
		i2.append([])
		for k2 in range(len(i[0])):
			sum = 0
			for k3 in range(len(kernel)):
				n = len(kernel) - 1 - k3
				for k4 in range(len(kernel[0])):
					m = len(kernel[0]) - 1 - k4
					jj = k1 + (k3 - kernel_centerY)
					ii = k2 + (k4 - kernel_centerX)
					if ((ii >= 0) and (ii < len(i)) and (jj >=0) and (jj < len(i[0]))):
						sum += i[ii][jj] * kernel[m][n]
			i2[k1].append(sum)
	i3 = numpy.array(i2)
	i3 = i3.T
	return i3

# Full Convolution of image I with kernel K

def convolution_dimensional(i,kernel):
	summa = []
	all_summs = []
	sum = 0
	kernel.reverse()
	for k1 in range(len(i)):
		for k2 in range(len(kernel)-1):
			i[k1].insert(0,0)
			i[k1].append(0)
		for k2 in range(len(i[k1])-len(kernel)+1):
			for k3 in range(len(kernel)):
				sum = kernel[k3]*i[k1][k3+k2] + sum
			summa.append(sum)
			sum = 0
		all_summs.append(summa)
		summa = []
	return all_summs

n = 20 #X
m = 10 #Y

i = []

# Случайное ч/б изображение 20x10

for k1 in range(m):
	i.append([])
	for k2 in range(n):
		i[k1].append(random.randint(0,1))

# Описать частные производные: d/dx, d/dy, d^2/dx^2, d^2/dy^2

# Примеры convolution: sobel operator, box filter (blur), gaussian blur
#		       sharpen, unsharp mask

# Описать интегралл изображения	

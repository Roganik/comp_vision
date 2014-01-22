# -*- coding: utf-8 -*-

import random

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

# Full Convolution of image I with kernel K

def convolution(i,kernel):
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

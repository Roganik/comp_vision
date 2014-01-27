# -*- coding: utf-8 -*-

import numpy as np

'''
Google it:
	* trackbar
	* hihgui tutorial
	* Partial differentials
	* image.shape
	* tentative numpy tutorial
	* opencv
	* scipy
'''

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

def convolution(image, kernel):
#                m   n
# (k*l)*[x,y] = SUM SUM k[i,j] * l[x-i,y-j]
#               j=1 i=1
	image = np.array(image)
	kernel = np.array(kernel)

	height, width = image.shape
	height_kern, width_kern = kernel.shape

	kernel_centerY = height_kern / 2
	kernel_centerX = width_kern / 2

	image2 = []
	sum = 0

	for y1 in range(height):
		image2.append([])
		for x1 in range(width):
			sum = 0
			for y2 in range(height_kern):
				n = height_kern - 1 - y2
				for x2 in range(width_kern):
					m = width_kern - 1 - x2
					ii = y1 + (y2 - kernel_centerY)
					jj = x1 + (x2 - kernel_centerX)
					if ((ii >= 0) and (ii < height) and (jj >=0) and (jj < width)):
						sum += image[ii][jj] * kernel[n][m]
			image2[y1].append(sum)
	return np.array(image2)

if __name__ == "__main__":
	tutorial2matrix = [[14, 7, 7, 6, 15, 20, 10],
	                   [14, 9, 13, 11, 2, 20, 2],
	                   [4, 2, 8, 9, 18, 6, 1],
	                   [19, 15, 1, 14, 4, 7, 20],
	                   [20, 2, 17, 10, 10, 3, 6],
	                   [6, 9, 5, 20, 11, 10, 8],
	                   [15, 3, 16, 2, 11, 19, 11]]

	tutorial2kernel1 = [[-1, 1]]
	tutorial2kernel2 = [[1, 0], [0, 1]]
	tutorial2kernel3 = [[1, 2, 3], [0, 0, -2], [5, 7, 11], [2, 3, 1]]
	print "Tutorial 2 convolution"
	print convolution(tutorial2matrix, tutorial2kernel1),"\n"
	print convolution(tutorial2matrix, tutorial2kernel2),"\n"
	print convolution(tutorial2matrix, tutorial2kernel3),"\n"

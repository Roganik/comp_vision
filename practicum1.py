# -*- coding: utf-8 -*-

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

def convolution(i,kernel):
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
					ii = k1 + (k3 - kernel_centerY)
					jj = k2 + (k4 - kernel_centerX)
					if ((ii >= 0) and (ii < len(i)) and (jj >=0) and (jj < len(i[0]))):
						sum += i[ii][jj] * kernel[n][m]
			i2[k1].append(sum)
	return i2

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

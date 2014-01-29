# -*- coding: utf-8 -*-

import numpy as np
import cv2

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

# http://docs.scipy.org/doc/scipy/reference/ndimage.html

def morphology_dilation(image, struct_element):

	image = np.array(image)
	struct_element = np.array(struct_element)

	height, width = image.shape
	height_struct, width_struct = struct_element.shape

	image2 = np.zeros((height,width), dtype = np.int)

	struct_element_centerY = height_struct / 2
	struct_element_centerX = width_struct / 2

	for y1 in range(height):
		for x1 in range(width):
			if (image[y1][x1] == 1):
				for y2 in range(height_struct):
					for x2 in range(width_struct):
						ii = y1 + y2 - struct_element_centerY
						jj = x1 + x2 - struct_element_centerX
						if (ii >= 0) and (ii < height) and (jj >=0) and (jj < width):
							image2[ii][jj] = max(image[ii][jj], struct_element[y2][x2])
	return image2

def morphology_erosion(image, struct_element):

	image = np.array(image)
	struct_element = np.array(struct_element)

	height, width = image.shape
	height_struct, width_struct = struct_element.shape

	image2 = np.zeros((height,width), dtype = np.int)

	struct_element_centerY = height_struct / 2
	struct_element_centerX = width_struct / 2

	for y1 in range(height):
		for x1 in range(width):
			sum = 0
			for y2 in range(height_struct):
				for x2 in range(width_struct):
					ii = y1 + y2 - struct_element_centerY
					jj = x1 + x2 - struct_element_centerX
					if (ii >= 0) and (ii < height) and (jj >=0) and (jj < width):
						if (image[ii][jj] == struct_element[y2][x2]):
							sum += 1
						if (sum == (height_struct * width_struct)):
							image2[y1][x1] = image[ii][jj]
						else:
							image2[y1][x1] = 0
	return image2

def morphology_opening(image, struct_element):

	image2 = morphology_erosion(image, struct_element)
	image3 = morphology_dilation(image2, struct_element)

	return image3

def morphology_closing(image, struct_element):

	image2 = morphology_dilation(image, struct_element)
	image3 = morphology_erosion(image2, struct_element)

	return image3


def partial_derivatives(image, a):

    if a == "dx":
        return convolution(image, [[1,-1]])
    elif a == "dy":
        return convolution(image, [[1],[-1]])


def element_multiply(image, image2):

        image = np.array(image)
	image2 = np.array(image2)

        height, width = image.shape
        height2, width2 = image2.shape

	if (height == height2) and (width == width2):
		for y in range(height):
			for x in range(width):
				image[y][x] *= image2[y][x]

	return image

def harris_corner_detector(image,kernel):

# Вычислить частные производные Ix Iy
	image_dx = partial_derivatives(image, "dx")
	image_dy = partial_derivatives(image, "dy")
# Вычислить поэлементные произведения: Ix^2, Iy^2, Ixy = Ix * Iy
	imageXX = element_multiply(image_dx, image_dx)
	imageYY = element_multiply(image_dy, image_dy)
	imageXY = element_multiply(image_dx, image_dy)
# Выполнить гауссово размытия для полученных матриц
	s_x = convolution(imageXX, kernel)
	s_y = convolution(imageYY, kernel)
	s_xy = convolution(imageXY, kernel)

	h, w = s_x.shape
	detector = np.zeros((h,w), dtype = np.int)
	determinant = 0
	trace = 0
	k = 0.05 # 0.04 - 0.06

# В каждой точке xy определить матрицу
# 	H = [
#	     [ s_x  , s_xy ]
#      	     [ s_xy , s_y  ]
#    	    ]
# Вычислить отклик детектора
	for y in range(h):
		for x in range(w):
			determinant = s_x[y][x] * s_y[y][x] - s_xy[y][x] * s_xy[y][x]
			trace = s_x[y][x] + s_y[y][x]
			detector[y][x] = determinant - k * (trace * trace)

# Применить подавление немаксимумов
	return detector

if __name__ == "__main__":
	image = cv2.imread("empire_state.jpg",2)
	kernel = [[0,1,0],
		  [1,4,1],
		  [0,1,0]]
	const = 0.125
	kernel = [[x * const for x in y ] for y in kernel]
	kernel = np.array(kernel)

	print kernel

	image2 = harris_corner_detector(image,kernel)
	print image2
	cv2.imshow("1",image)
	cv2.imshow("2", image2)
	cv2.waitKey()

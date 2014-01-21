# -*- coding: utf-8 -*-

import random

# Определить массив в котором хранить изображение
# Может состоять из (0...1), (0...255), ([0...255], [0...255], [0...255])

n = 20
m = 10

i = []

# Случайное ч/б изображение

for k1 in range(n):
	i.append([])
	for k2 in range(m):
		i[k1].append(random.randint(0,1))

# Описать частные дифференциалы: d/dx, d/dy, d^2/dx^2, d^2/dy^2

# Описать Convolution изображения с ядром k

# Описать частные производные: d/dx, d/dy, d^2/dx^2, d^2/dy^2

# Примеры convolution: sobel operator, box filter (blur), gaussian blur
#		       sharpen, unsharp mask

# Описать интегралл изображения	

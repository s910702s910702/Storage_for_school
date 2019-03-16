import sys
import random as rd
import numpy as np

def open_data(which):
	file = open(which, "r")
	data = []

	for i in file:
		tmp = i.split()
		tmp_data = []

		for t in tmp:
			tmp_data.append(eval(t))

		x = np.matrix([1] + tmp_data[:-1])
		y = np.matrix(tmp_data[-1])

		data.append((x, y))

	return data


def main():
	dataes = open_data("data1.txt")

	learning_rate = 0.00005
	max_iteration = 2000
	w = np.full_like(dataes[0][0], rd.random(), dtype='float64')

	for it in range(max_iteration):
		for data in dataes:
			(x, y) = data

			w += learning_rate * 2. * (y - w * x.transpose()) * x

	print(w)

main()
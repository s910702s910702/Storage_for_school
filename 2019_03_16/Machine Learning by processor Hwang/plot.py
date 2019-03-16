import sys
import random as rd
import numpy as np
import matplotlib.pyplot as plt


def open_data(which):
	file = open(which, "r")
	data = []

	for i in file:
		tmp = i.split()
		tmp_data = []

		for t in tmp:
			tmp_data.append(eval(t))

		data.append(tmp_data)

	return data

def main():
	datas = open_data('data1.txt')

	for data in datas:
		x = data[0]
		y = data[-1]
		plt.plot(x, y, 'o')

	x = [i for i in range(100)]
	y = [21.44437957 + 3.98593656 * i for i in x]
	plt.plot(x, y)

	plt.show()


main()
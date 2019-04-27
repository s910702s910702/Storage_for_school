import sys
import numpy as np
import random as rd
import checker
import inputer

import multiprocessing as mp

def sigmoid(x):
	return 1 / (1 + np.exp(-x))


# calculate the output of the nn, and return delta of output layer
def work(data):
	(data, mw, mu) = data
	(x, y) = data

	# forward
	x = [1] + x
	o1 = sigmoid(np.matrix(x) * np.matrix(mw).transpose()).tolist()[0]

	tmp = [1] + o1
	o2 = sigmoid(np.matrix(tmp) * np.matrix(mu).transpose()).tolist()[0]


	# make delta
	# delta = o * o' * (y - o)
	delta_o = []
	for i in range(len(o2)):
		if y[i] == 1:
			delta_o.append(o2[i] * (1 - o2[i]) * (0.9 - o2[i]))
		else:
			delta_o.append(o2[i] * (1 - o2[i]) * (0.1 - o2[i]))

	tmp_h = (np.matrix(delta_o) * np.matrix(mu)).tolist()[0][1:]

	delta_h = []
	for i in range(len(tmp_h)):
		delta_h.append(o1[i] * (1 - o1[i]) * tmp_h[i])

	# backward
	do = np.matrix(delta_o).transpose() * np.matrix(tmp)
	dh = np.matrix(delta_h).transpose() * np.matrix(x)

	return dh, do

def main():
	# ni, nh, no, [path to input and output], max_epoch, learning rate
	ni, nh, no, which, max_epoch, lr = eval(sys.argv[1]), eval(sys.argv[2]), eval(sys.argv[3]), sys.argv[4], eval(sys.argv[5]), eval(sys.argv[6])

	mw = [[rd.uniform(-0.1, 0.1) for i in range(ni + 1)] for j in range(nh)]
	mu = [[rd.uniform(-0.1, 0.1) for i in range(nh + 1)] for j in range(no)]


	data = inputer.inputer(which)
	pool = mp.Pool()

	for i in range(max_epoch):
		if i % 1000 == 0:
			print(i, ":")
			print("mw:\n", mw)
			print("mu:\n", mu)
			checker.checker(data, mw, mu)

		result = pool.map(work, [(d, mw, mu) for d in data])

		sum_dh = np.matrix([[0. for _ in range(ni + 1)] for _ in range(nh)])
		sum_do = np.matrix([[0. for _ in range(nh + 1)] for _ in range(no)])
		
		for r in result:
			dh, do = r
			sum_do += do
			sum_dh += dh

		sum_do /= len(result)
		sum_dh /= len(result)


		# update weight
		mu = mu + lr * sum_do
		mw = mw + lr * sum_dh

	print("FINAL:")
	checker.checker(data, mw, mu)

if __name__ == '__main__':
	main()


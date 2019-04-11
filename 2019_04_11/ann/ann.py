import numpy as np
import random as rd
import inputer as ip
import checker as chk

# This sigmoid cannot apply to list
def sigmoid(x):
	return 1 / (1 + np.exp(-x))


def forward(inp, wei):
	inp = [1] + inp
	result = np.matrix(inp) * np.matrix(wei).transpose()

	# sigmoid
	result = sigmoid(result)

	return result.tolist()[0]


def make_delta(y, o2, o, mu):
	do = []
	for i in range(len(o2)):
		if y[i] == 1:
			do.append(o2[i] * (1 - o2[i]) * (0.9 - o2[i]))
		else:
			do.append(o2[i] * (1 - o2[i]) * (0.1 - o2[i]))
		# do.append(o2[i] * (1 - o2[i]) * (y[i] - o2[i]))


	tmp = (np.matrix(do).transpose() * np.matrix(mu)).tolist()[0][1:]
	dh = []
	for i in range(len(tmp)):
		dh.append(o[i] * (1 - o[i]) * tmp[i])

	return do, dh


# Because we only using sigmoid function, we use O * O' * (y-O)
def backward(inp, d, wei, lr):

	inp = [1] + inp
	wei = np.matrix(wei) + lr * np.matrix(d).transpose() * np.matrix(inp)

	return np.array(wei)


def Backpropagation(inputs, ni, nh, no, lr):
	mw = [[rd.uniform(-0.1, 0.1) for i in range(ni + 1)] for j in range(nh)]
	mu = [[rd.uniform(-0.1, 0.1) for i in range(nh + 1)] for j in range(no)]

	max_epoch = 200000

	for i in range(max_epoch):
		if i % 1000 == 0:
			print(i, ":")
			chk.checker(inputs, mw, mu)

		for inp in inputs:
			x, y = inp

			o = forward(x, mw)
			o2 = forward(o, mu)

			do, dh = make_delta(y, o2, o, mu)

			mu = backward(o, do, mu, lr)
			mw = backward(x, dh, mw, lr)

		np.random.shuffle(inputs)

	return mw, mu


# main
learning_rate = 0.1
input_matrix = ip.inputer("1-2.txt")
print(input_matrix)

mw, mu = Backpropagation(input_matrix, 4, 3, 1, learning_rate)

print("FINAL:")
print("mw:\n", mw)
print("mu:\n", mu)
print("--------------------------")

chk.checker(input_matrix, mw, mu)

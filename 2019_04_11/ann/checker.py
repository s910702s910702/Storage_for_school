import numpy as np

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def checker(inputs, mw, mu):
	correct = 0
	error = 0

	for inp in inputs:
		(x, y) = inp
		x = [1] + x

		o1 = sigmoid(np.matrix(x) * np.matrix(mw).transpose()).tolist()[0]
		# print(o1)

		o1 = [1] + o1
		o2 = sigmoid(np.matrix(o1) * np.matrix(mu).transpose()).tolist()[0]
		print(x[1:], y, [format(o2[0], ".6f")], end = '')

		if (y[0] == 0 and o2[0] >= 0.5) or (y[0] == 1 and o2[0] < 0.5):
			error += 1
			print("\tΣ -`д´-")
		else:
			correct += 1
			print("")

	print("--------------------")
	print("Result: ", error, "errors in", error + correct, "total.")

if __name__ == '__main__':
	x = [([1, 0], [1])]
	mw = [-1.11182468, 8.6392916, 8.68045026]
	mu = [-5.32542919, 5.99874398]
	checker(x, mw, mu)
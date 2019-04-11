# for input function

def inputer(where):
	file = open(where, "r")

	final = []

	for line in file:
		l = line.split()

		x = [eval(l[0][i]) for i in range(len(l[0]))]
		y = [eval(l[1])]

		final.append((x, y))

	return final

def main():
	path = "1-1.txt"

	inputer(path)

if __name__ == '__main__':
	main()
def process_train_anxiety():
	file = open("../training/train2.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-1]))
		x = [int(i) for i in x]
		x = x[0:5]
		xs.append(x)
	return [xs, ys]

def process_eval_anxiety():
	file = open("../training/eval2.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-1]))
		x = [int(i) for i in x]
		x = x[0:5]
		xs.append(x)
	return [xs, ys]

def process_test_anxiety():
	file = open("../training/test2.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-1]))
		x = [int(i) for i in x]
		x = x[0:5]
		xs.append(x)
	return [xs, ys]

def process_train_depression():
	file = open("../training/train2.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-2]))
		x = [int(i) for i in x]
		x = x[0:5]
		xs.append(x)
	return [xs, ys]

def process_eval_depression():
	file = open("../training/eval2.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-2]))
		x = [int(i) for i in x]
		x = x[0:5]
		xs.append(x)
	return [xs, ys]

def process_test_depression():
	file = open("../training/test2.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-2]))
		x = [int(i) for i in x]
		x = x[0:5]
		xs.append(x)
	return [xs, ys]

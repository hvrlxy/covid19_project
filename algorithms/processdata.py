def process_train_anxiety():
	file = open("../training/train.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-1]))
		x = [int(x[0]), int(x[1]), int(x[2]), int(x[3]),int(x[4])]
		x = [int(i) for i in x]
		xs.append(x)
	return [xs, ys]

def process_eval_anxiety():
	file = open("../training/eval.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-1]))
		x = [int(x[0]), int(x[1]), int(x[2]), int(x[3]),int(x[4])]
		x = [int(i) for i in x]
		xs.append(x)
	return [xs, ys]

def process_test_anxiety():
	file = open("../training/test.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-1]))
		x = [int(x[0]), int(x[1]), int(x[2]), int(x[3]),int(x[4])]
		x = [int(i) for i in x]
		xs.append(x)
	return [xs, ys]

def process_train_depression():
	file = open("../training/train.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-2]))
		x = [int(x[0]), int(x[1]), int(x[2]), int(x[3]),int(x[4])]
		x = [int(i) for i in x]
		xs.append(x)
	return [xs, ys]

def process_eval_depression():
	file = open("../training/eval.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-2]))
		x = [int(x[0]), int(x[1]), int(x[2]), int(x[3]),int(x[4])]
		x = [int(i) for i in x]
		xs.append(x)
	return [xs, ys]

def process_test_depression():
	file = open("../training/test.txt")
	lines = file.readlines()
	xs = []
	ys = []
	for line in lines:
		line = line.replace('\n', '').replace('[','').replace(']','')
		x = line.split(', ')
		ys.append(int(x[-2]))
		x = [int(x[0]), int(x[1]), int(x[2]), int(x[3]),int(x[4])]
		x = [int(i) for i in x]
		xs.append(x)
	return [xs, ys]

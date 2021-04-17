import random

file = open("../data/restricted_data.txt")
lines = file.readlines()
total = len(lines)

isChosen = [False] * total
#print(isChosen)

#pick the training set
train = 0
while (train < 4600):
	i = random.randint(0, 6628)
	if isChosen[i] == False:
		train = train + 1
		print(lines[i].replace('\n', ''))
		isChosen[i] = True

print('\n')

#pick the eval set
val = 0
while (val < 1000):
	i = random.randint(0, 6628)
	if isChosen[i] == False:
		val = val + 1
		print(lines[i].replace('\n', ''))
		isChosen[i] = True

print('\n')

for i in range(total):
	if isChosen[i] == False:
		print(lines[i].replace('\n', ''))

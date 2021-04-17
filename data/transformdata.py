file = open("alldata.csv", 'r')
lines = file.readlines()
for line in lines:
	data = line.split(',')
	new_line = []
	valid = True
	for l in data:
		if l == "":
			valid = False
	if valid:
		if data[0] == "Single":
			new_line.append(0)
		else:
			new_line.append(1)

		if data[-7] == '0%':
			new_line.append(0)
		elif data[-7] == '1-29%':
			new_line.append(1)
		elif data[-7] == '30-59%':
			new_line.append(2)
		else:
			new_line.append(3)

		if data[-6] == '20-29':
			new_line.append(1)
		elif data[-6] == '30-49':
			new_line.append(2)
		elif data[-6] == '50+':
			new_line.append(3)
		else:
			new_line.append(0)

		new_line.append(int(data[-5]))
		new_line.append(int(data[-4]))
		new_line.append(int(data[-2]))
		new_line.append(int(data[-1]))

		print(new_line)


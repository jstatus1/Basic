def fibonacci(firstValue, secondValue, termLimit):
	sequence = [firstValue, secondValue]

	for i in range(termLimit - 2):
		sequence.append(sequence[i] + sequence[i +1]) 

	return sequence

print(fibonacci(6,3,10))
print(fibonacci(2,6,10))


def fibonnaciGrid(steps):
	sequence = [["cat"]]

	for i in range(steps):
		for j in range(steps):
			if (sequence[i][j] == 
				sequence[i][j]
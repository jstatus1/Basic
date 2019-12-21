
previousNumber = 1
currentNumber = 2
evenCounter = 1
for i in range(3, 91):
	nextNumber = previousNumber + currentNumber
	if nextNumber > 10:
		nextNumber = nextNumber - 10
		previousNumber = currentNumber
		currentNumber = nextNumber
	else:
		previousNumber = currentNumber
		currentNumber = nextNumber

	if(currentNumber % 2) == 0:
		evenCounter += 1
	
	print(f"Index: {i} , Current Number: {currentNumber}")

print(evenCounter)

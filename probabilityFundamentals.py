import random



def expectedSingleDice():
	averageSum = 0
	for i in range(1, 20000):
		int1 = random.randint(1,6)
		
		previousSum = 0
		
		if i == 1:
			averageSum = ((int1)/i)
			print(f"int1: {int1}" + f" averageSum: {averageSum}")
		else:
			averageSum = (((int1) + (averageSum * (i - 1)))/(i))
			print(f"int1: {int1}" + f" averageSum: {averageSum}")

	return averageSum
	

#print(expectedSingleDice())

def arithmeticSeq(firstTerm, lastIndex, commonDif):
	
	return firstTerm + ((lastIndex - 1) * commonDif)




def lotteryChances():


def longest(s):
	LongestStr = ''
	CurrentStr  = ''
	previousChar, currentChar = '', ''

	for letter in s:
		if currentChar == '':
			currentChar = letter
			CurrentStr = CurrentStr
		if previousChar == '':
			previousChar = letter

		currentChar = letter

		#print (f"{previousChar} : {currentChar}")
		if(ord(currentChar) >= ord(previousChar)):
			CurrentStr += letter
			#print (f"CurrentStr: {CurrentStr}")
			if len(LongestStr) < len(CurrentStr):
				LongestStr = CurrentStr
		else:
			CurrentStr = letter
			#print (f"CurrentStr: {CurrentStr}")
			
		previousChar = letter
			


	return LongestStr



	
print (longest('asdfaaaabbbbcttavvfffffdf'))

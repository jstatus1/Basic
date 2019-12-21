def maxSequence(arr):
	maxSum = 0
	for i in range(len(arr)):
		for j in reversed(range(len(arr))):
			branchArr = arr[i:j+1]
			print(f"BranchArr: {branchArr}")
			nextSum = sum(branchArr)
			if nextSum > maxSum:
				maxSum = nextSum
	return maxSum
			



print (maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
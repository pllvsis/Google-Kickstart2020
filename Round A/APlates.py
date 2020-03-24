totalCases = 0
testcase = []

def sumTillMax(i, arr, max):
	ind = 0
	for i in range(len(arr)):
		if arr[i] == max:
			ind = i
	sum = 0
	for i in range(ind + 1):
		sum += arr[i]
	return [ i, ind, sum ]

def sumTillNum(i, arr, num):
	sum = 0
	for i in range(arr.index(num) + 1):
		sum += arr[i]
	ind = arr.index(num) + 1
	return [ i, ind, sum ]

totalCases = int(input())

for i in range(totalCases):
	case = []
	N, K, P = input().split()
	case.append(int(N))
	case.append(int(K))
	case.append(int(P))
	stacks = []
	for i in range(int(N)):
		value = [int(x) for x in input().split()]
		stacks.append(value)
	case.append(stacks)
	testcase.append(case)



for case in testcase:
	stacksMaxValue = []
	numOfStack, stackCount, plates = case[0], case[1], case[2]
	stacks = case[3]
	for i in range(len(stacks)):
		stacksMaxValue.append(sumTillMax(i, stacks[i], max(stacks[i])))
	stacksMaxValue.sort(key = lambda x: x[2], reverse = 1)
	counter = 0
	usedStack = []
	beautyCount = 0
	while plates >= 0 and counter < numOfStack - 1:
		if (plates - (stacksMaxValue[counter][1] + 1) >= 0):
			plates -= (stacksMaxValue[counter][1] + 1)
			beautyCount += stacksMaxValue[counter][2]
			usedStack.append(stacksMaxValue[counter][0])
			stacksMaxValue.pop(0)
		counter += 1

	if plates == 0:
		print("Case #" + str(testcase.index(case) + 1) + ": " + str(beautyCount))
	else:
		stackList = [x for x in range(0, numOfStack)]
		remainingStack = [i for i in stackList if i not in usedStack]
		stacksMaxValue = []
		for i in remainingStack:
			stacksMaxValue.append(sumTillNum(i, stacks[i], stacks[i][plates - 1]))
		stacksMaxValue.sort(key = lambda x: x[1], reverse = 1)
		beautyCount += stacksMaxValue[0][2]
		print("Case #" + str(testcase.index(case) + 1) + ": " + str(beautyCount))

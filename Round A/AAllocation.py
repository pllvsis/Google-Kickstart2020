totalCases = 0
testcase = []

totalCases = int(input())

for i in range(totalCases):
	N, B = input().split()
	costs = [int(x) for x in input().split()]
	costs.sort()
	house = []
	house.append(int(N))
	house.append(int(B))
	house.append(costs)
	testcase.append(house)

for house in testcase:
	N = house[0]
	B = house[1]
	costs = house[2]
	counter = 0
	while B > 0:
		if counter > N - 1:
			break
		print(counter)
		B = B - costs[counter]
		counter += 1
	if B < 0:
		print("Case #" + str(testcase.index(house) + 1) + ": " + str(counter - 1))
	else:
		print("Case #" + str(testcase.index(house) + 1) + ": " + str(counter))

# Print Path
def printPath(res):
	total = sum(res)
	li.append(res)

# To find max Coins
def maxcoins(arr, row, col, res):
	# If we have reached the last cell
	if (row == len(arr)-1 and col == len(arr[0])-1):
		printPath(res+[1])
		return
	# Include current cell in res
	res.append(arr[row][col])
	# Move right
	if (row >= 0 and col < len(arr) and col+1 > 0 and col+1 < len(arr[0])):
		maxcoins(arr, row, col+1, res)

	# Move down
	if (row+1 >= 0 and row+1 < len(arr) and col >= 0 and col < len(arr[0])):
		maxcoins(arr, row+1, col, res)

	# Remove current cell from res
	res.pop(-1)


# To find the number of all possible paths
def numberOfPaths(i, j):
	if(i == 1 or j == 1):
		return 1
	return numberOfPaths(i-1, j) + numberOfPaths(i, j-1)

# data inputs
rows = 3
cols = 4
arr = [[0,3,1,1],[2,0,0,4],[1,5,3,1]]
res = []
global li
li = []
totalPaths = numberOfPaths(rows, cols)
maxcoins(arr, 0, 0, res)
noOfCoins = []
for i in range(totalPaths):
	tot = sum(li[i])
	noOfCoins.append(tot)
index = [i for i, j in enumerate(noOfCoins) if j == max(noOfCoins)]
for x in index:
	print(li[x], " have max coins i.e ", max(noOfCoins))

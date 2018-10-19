def print_me(arr):
	for i in arr:
		print(i)
	print()

bpGraph =[[0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1]]

newGraph = []
for i in bpGraph:
	temp = []
	for j in i:
		temp.append(j)
	newGraph.append(temp)

# Set source and target
resGraph = []
for i in range(len(newGraph)):
	temp = [0]*(len(newGraph)*2)
	for j in range(len(newGraph)):
		if newGraph[i][j] == 1:
			temp[j + len(newGraph)] = 1
	resGraph.append(temp)

resGraph = resGraph + [[0]*(len(newGraph)*2)]*len(newGraph)

temp = [0] + [1]*len(bpGraph) + [0]*(len(bpGraph) + 1)
resGraph = [temp] + resGraph
resGraph = resGraph + [[0]*(len(resGraph) + 1)]

for i in range(len(resGraph)):
	if i != 0 and i != len(resGraph) - 1:
		if i < len(resGraph)/2:
			resGraph[i] = [0] + resGraph[i] + [0]
		else:
			resGraph[i] = [0] + resGraph[i] + [1]

ref_Graph = []
for i in resGraph:
	temp = []
	for j in i:
		temp.append(j)
	ref_Graph.append(temp)
# Initialize labels for Preflow
label = []
excess = [0]*len(resGraph)
label.append(len(resGraph))
label.extend([0 for x in range(len(resGraph)) if x != 0])

def push(v, w):
	if excess[v] > 0 and label[v] > label[w] and resGraph[v][w] > 0:
		q = min(excess[v] , resGraph[v][w])
		resGraph[v][w] -= q
		resGraph[w][v] += q
		excess[w] += q
		excess[v] -= q
		return 256
	else:
		return 0

def relabel(v):
	if excess[v] > 0:
		label[v] += 1

for i in range(len(resGraph)):
	if i != 0 and resGraph[0][i] != 0:
		resGraph[i][0] += resGraph[0][i]
		excess[i] = resGraph[0][i]
		resGraph[0][i] -= resGraph[i][0]

while not all(x == 0 for x in excess[1:len(resGraph) - 1]):
	src_node = [i for i in range(1,len(excess) - 1) if excess[i] > 0][0]
	next_node = [i for i,x in enumerate(resGraph[src_node]) if x > 0]
	j = 0
	flag = 0
	while j < len(next_node):
		temp = next_node[j]
		tempPush = push(src_node, temp)
		if tempPush == 0:
			j += 1
			continue
		else:
			flag = 1
			break
	if flag == 0:
		relabel(src_node)

pairs = []
for i in range(len(resGraph)):
	for j in range(len(resGraph)):
		if i != 0 and j != 0 and i != len(resGraph) - 1 and j != len(resGraph) - 1 and ref_Graph[i][j] == 1 and resGraph[i][j] == 0:
			pairs.append((i,j - len(bpGraph)))

print('Number of pairs : ' + str(excess[len(resGraph) - 1]))
print('The formed pairs:', pairs)

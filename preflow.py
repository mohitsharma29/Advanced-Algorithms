#graph = [[0,16,13,0,0,0], [0,0,10,12,0,0], [0,4,0,0,14,0], [0,0,9,0,0,20], [0,0,0,7,0,4] , [0,0,0,0,0,0]]
graph = [[0,6,6,0], [0,0,1,5], [0,0,0,5], [0,0,0,0]]
#graph = [[0,3,2], [0,0,2], [0,0,0]]
resGraph = graph[:]

# Initialize lables for Preflow
label = []
excess = [0]*len(graph)
label.append(len(graph))
label.extend([0 for x in range(len(graph)) if x != 0])

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

for i in range(len(graph)):
	if i != 0 and resGraph[0][i] != 0:
		resGraph[i][0] += resGraph[0][i]
		excess[i] = resGraph[0][i]
		resGraph[0][i] -= resGraph[i][0]

while not all(x == 0 for x in excess[1:len(graph) - 1]):
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

print(excess[len(graph) - 1])
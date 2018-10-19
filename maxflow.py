"""graph = [[0, 9, 9, 0, 0, 0],
        [0, 0, 4, 8, 0, 0],
        [0, 0, 0, 1, 3, 0],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 8, 0, 7],
        [0, 0, 0, 0, 0, 0]]"""
graph = [[0, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 2, 0],
[0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0]]

oldGraph = []
for i in graph:
	temp = []
	for j in i:
		temp.append(j)
	oldGraph.append(temp)

def bfs(s,t,parent):
	queue = []
	visited = [False]*len(graph)
	queue.append(s)
	visited[s] = True
	while queue:
		temp = queue.pop(0)
		visited[temp] = True
		for i in range(len(graph[temp])):
			if graph[temp][i] > 0 and visited[i] == False:
				queue.append(i)
				visited[i] =True
				parent[i] = temp
	return True if visited[t] else False

def FordFul(source,sink):
	parent = [-1]*len(graph)
	max_flow = 0
	paths = []
	while bfs(source,sink, parent):
		path_flow = float("Inf")
		s = sink
		tempPath = []
		while(s != source):
			path_flow = min(path_flow, graph[parent[s]][s])
			tempPath.append([parent[s], s])
			s = parent[s]
		max_flow += path_flow
		v = sink
		paths.append(tempPath)
		while v != source:
			u = parent[v]
			graph[u][v] -= path_flow
			graph[v][u] += path_flow
			v = parent[v]
	return paths,max_flow

paths, maxFlow = FordFul(0,5)
print(maxFlow)
orgFlow = []
for i in range(len(graph)):
	orgFlow.append([0]*len(graph))

for i in range(len(orgFlow)):
	for j in range(len(orgFlow)):
		for k in paths:
			for l in k:
				if l == [i,j]:
					orgFlow[i][j] += graph[i][j]


print("Maxflow, Final Flow")
print(maxFlow,orgFlow)
tempGraph = []
for i in graph:
	temp = []
	for j in i:
		temp.append(j)
	tempGraph.append(temp)

def incFlow(x):
	global graph
	flag = -1
	incre_path = [-1,-1]
	for i in range(len(graph)):
		for j in range(len(graph)):
			if oldGraph[i][j] != 0 and graph[i][j] == 0:
				graph[i][j] += x
				newPath, newFlow = FordFul(0,5)
				if newFlow == x:
					incre_path = [i,j]
					flag = 1
					break
				else:
					graph = []
					for i1 in tempGraph:
						temp = []
						for j1 in i1:
							temp.append(j1)
						graph.append(temp)
		if flag == 1:
			break
	return incre_path

print("Increased flow at edge: ")
print(incFlow(5))

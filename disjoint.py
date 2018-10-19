graph = [[0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0]];

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

pathy = []
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
		tempPath.reverse()
		pathy.append(tempPath)
		max_flow += path_flow
		v = sink
		paths.append(tempPath)
		while v != source:
			u = parent[v]
			graph[u][v] -= path_flow
			graph[v][u] += path_flow
			v = parent[v]
	return paths,max_flow

paths, maxFlow = FordFul(0,len(graph) - 1)

print("Maximum edge disjoint paths: " + str(maxFlow))
[print(x) for x in pathy]
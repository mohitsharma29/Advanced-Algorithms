graph = [
[0,1,1,0,0],
[1,0,1,1,0],
[1,1,0,1,0],
[0,1,1,0,1],
[0,0,0,1,0]
]
N = len(graph)
numCols = 6
solution = [-1]*N

def Color(graph, cn, count):
    if count == N:
        return True
    for i in range(cn):
        if check(count, i, graph):
            solution[count] = i
            status = Color(graph, cn, count + 1)
            if status == True:
                return True
            else:
                solution[count] = -1
                continue
        else:
            continue
    return False

def check(count, i, graph):
    for j in range(N):
        if graph[count][j] == 1 and solution[j] == i:
            return False
    return True

for x in range(numCols):
    status = Color(graph,x + 1,count = 0)
    if status == True:
        break

print(solution)

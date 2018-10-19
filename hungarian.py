def print_me(arr):
	for i in arr:
		print(i)
	print()

def biMatch(bpGraph):
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
            if newGraph[i][j] > 0:
                temp[j + len(newGraph)] = newGraph[i][j]
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

    return excess[len(resGraph) - 1], resGraph, ref_Graph

def findNext(m,residual):
    retSet = []
    for i in range(len(residual[m])):
        if residual[m][i] != 0:
            retSet.append(i)
    return retSet

def mincut(residual):
    s = []
    t = []
    i = 0
    k = -1
    while i < len(residual):
        if i in s:
            i += 1
            continue
        elif residual[0][i] != 0:
            s.append(i)
        else:
            i += 1
            continue
        j = []
        j.append(i)
        k += 1
        counter = 0
        visited = []
        visited.append(0)
        while True:
            if k == -1:
                break
            nextNeb = findNext(j[k], residual)
            visited.append(j[k])
            del j[k]
            k -= 1
            if nextNeb == [] and k == -1:
                break
            else:
                temp = [x for x in nextNeb if x not in s]
                s.extend(temp)
                temp = [x for x in nextNeb if x != 0 and x not in visited]
                j.extend(temp)
                k += len(temp)
                counter += 1
        i += 1

    for i in range(len(residual)):
        if i not in s and i != 0 and i != len(residual) - 1:
            t.append(i)
    s = [x for x in s if x != 0]
    return s,t

def vertexCov(s,maxMat):
    len_graph = len(maxMat)
    original = [x for x in range(len_graph)]
    l = original[1:int(len_graph/2)]
    r = original[int(len_graph/2):len_graph - 1]
    s = set(s)
    l = set(l)
    r = set(r)
    l1 = l.intersection(s)
    l2 = l.difference(s)
    r1 = r.intersection(s)
    r2 = r.difference(s)
    b = []
    for i in r2:
        temp = []
        for j in range(len(maxMat[i])):
            if maxMat[i][j] == 1:
                if j in l1:
                    temp.append(j)
        b.extend(temp)
    b = set(b)
    v = ((l2.union(r1)).union(b))
    return v

def computeCost(residualGraph):
    summy = 0
    for i in range(len(residualGraph)):
        for j in range(len(residualGraph)):
            if i > 0 and i >= len(residualGraph)/2:
                if residualGraph[i][j] == 1 and residualGraph[j][i] > 0:
                    summy += residualGraph[j][i] + 1
    return summy

#pairs, residualGraph = biMatch(a1)

"""
while pairs != len(costMat):
    s,t = mincut(residualGraph)
    v = vertexCov(s, len(costMat)*2)

print(computeCost(residualGraph))"""
# print_me(residualGraph)
"""
testG = [
[0,1,1,0,0,0],
[0,0,1,1,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]
]"""
"""
testbg = [
[1,0,0],
[5,6,7],
[5,0,0]
]
"""
"""
pairs, residualGraph, ref_Graph = biMatch(testbg)
print(pairs)
print_me(residualGraph)
print_me(ref_Graph)
s,t = mincut(residualGraph)
print("mincut" , s,t)
print(vertexCov(s,ref_Graph))"""

costMat = [[1,4,5],[5,7,6], [5,8,8]]

a0 = []
for i in costMat:
    temp = []
    for j in i:
        temp.append(j)
    a0.append(temp)

for i in a0:
    temp = min(i)
    i[:] = [x - temp for x in i]

for i in range(len(a0)):
    temp = min([a0[x][i] for x in range(len(a0))])
    for j in range(len(a0)):
        a0[j][i] -= temp
#print(a0)
a1 = []
for i in range(len(a0)):
    temp = []
    for j in range(len(a0)):
        if a0[i][j] == 0 and costMat[i][j] != 0:
            temp.append(costMat[i][j])
        else:
            temp.append(0)
    a1.append(temp)

copyCost = []
for i in a1:
    temp = []
    for j in i:
        temp.append(j)
    copyCost.append(temp)

pairs, residualGraph, ref_Graph = biMatch(copyCost)
while True:
    #print(pairs)
    if pairs == len(costMat):
        break
    s,t = mincut(residualGraph)
    vcov = vertexCov(s,ref_Graph)
    """
    points = []
    for i in vcov:
        if i > len(costMat):
            points.append(i - len(costMat) - 1)
        else:
            points.append(i - 1)"""
    minimum = 25000
    #print(vcov)
    for i in range(len(a0)):
        for j in range(len(a0)):
            if i + 1 not in vcov and j + len(costMat) + 1 not in vcov:
                if a0[i][j] < minimum:
                    minimum = a0[i][j]
    for i in range(len(a0)):
        for j in range(len(a0)):
            if i + 1 in vcov and j + 1 + len(costMat) in vcov:
                a0[i][j] += minimum
            elif i + 1 not in vcov and j + len(costMat) + 1 not in vcov:
                a0[i][j] -= minimum
    #print(a0)
    pairs, residualGraph, ref_Graph = biMatch(a0)
    print_me(ref_Graph)
    print(pairs)
    break

print(pairs)

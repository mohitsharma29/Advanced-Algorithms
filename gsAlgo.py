menMatch = {}
womMatch = {}
prefMen = {}
prefWom = {}
N = 4

"""prefer = [[7, 5, 6, 4],[5, 4, 6, 7],[4, 5, 6, 7],[4, 5, 6, 7],[0, 1, 2, 3],[0, 1, 2, 3],[0, 1, 2, 3],[0, 1, 2, 3]]"""

for i in range(N):
	menMatch[i] = -1
	womMatch[i] = -1
	"""prefMen[i] = [x - 4 for x in prefer[i]]
	prefWom[i] = prefer[i + 4]"""

prefMen = {
	0:[2,1,3,0],
	1:[1,2,0,3],
	2:[2,0,1,3],
	3:[2,1,3,0]
}

prefWom = {
	0:[3,2,0,1],
	1:[1,0,2,3],
	2:[0,2,3,1],
	3:[3,2,0,1]
}

while -1 in menMatch.values():
	i = 0
	temp = 0
	while i < N:
		if menMatch[i] != -1:
			i += 1
			temp = 0
		else:
			if prefMen[i][temp] != -1:
				tempWom = prefMen[i][temp]
				if womMatch[tempWom] == -1:
					menMatch[i] = tempWom
					womMatch[tempWom] = i
					i += 1
					temp = 0
				else:
					curMat = womMatch[tempWom]
					index_cur = 0
					index_i = 0
					for j in range(len(prefWom[tempWom])):
						if prefWom[tempWom][j] == curMat:
							index_cur = j
						if prefWom[tempWom][j] == i:
							index_i = j
					if index_i < index_cur:
						tempy = womMatch[tempWom]
						menMatch[i] = tempWom
						womMatch[tempWom] = i
						menMatch[tempy] = -1
						i += 1
						temp = 0
					else:
						prefMen[i][temp] = -1
						temp += 1
			else:
				temp += 1

avg_men = 0
avg_wom = 0
for i in prefMen:
	for j in range(len(prefMen[i])):
		if prefMen[i][j] == menMatch[i]:
			avg_men += j + 1

for i in prefWom:
	for j in range(len(prefWom[i])):
		if prefWom[i][j] == womMatch[i]:
			avg_wom += j + 1

avg_men /= N
avg_wom /= N


print("Men", menMatch)
print("Women", womMatch)
print("Average choice of men is " + str(avg_men))
print("Average choice of woman is " + str(avg_wom))
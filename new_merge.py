def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def pairwise(it):
    it = iter(it)
    while True:
        yield next(it), next(it)


arr = [20, 12, 15, 16, 9, 7, 17, 11, 6, 3, 19, 13, 2, 4, 10, 1, 18, 14, 8, 5]
points = []
i = 0

while i < len(arr):
	current_index = i
	if i + 1 < len(arr) and arr[i] < arr[i + 1]:
		while i + 1 < len(arr) and arr[i] <= arr[i + 1]:
			i += 1
		points.append(arr[current_index:i + 1])
		i += 1
	else:
		while i + 1 < len(arr) and arr[i] > arr[i + 1]:
			i += 1
		points.append(arr[current_index:i + 1][::-1])
		i += 1

print(points)

while True:
	temp_list = []
	for a,b in pairwise(points):
		temp_list.append(merge(a,b))
	points = temp_list
	if len(points) == 1:
		break

print(points[0])
#Optimal 7, greedy 8
n = [2,3,4,6,2,2]
new_n = sorted(n, reverse=True)
m = 3
machine_loads = {}
new_loads = {}

for i in range(m):
    machine_loads[i] = []
    new_loads[i] = []

for i in range(len(n)):
    if i < m:
        machine_loads[i].append(n[i])
        new_loads[i].append(new_n[i])
    else:
        minIndex = min(machine_loads, key=lambda x: sum(machine_loads[x]))
        tempIndex = min(new_loads, key=lambda x: sum(new_loads[x]))
        machine_loads[minIndex].append(n[i])
        new_loads[tempIndex].append(new_n[i])

print(machine_loads)
makespan = sum(machine_loads[max(machine_loads, key=lambda x: sum(machine_loads[x]))])
print("makespan is ", makespan)

print("Sorted version")
new_makespan = sum(new_loads[max(new_loads, key=lambda x: sum(new_loads[x]))])
print(new_loads)
print("new makespan is ", new_makespan)

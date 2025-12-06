import numpy as np

file = open("input.txt")
lines = file.read().splitlines()

data = []
for text in lines[:-1]:
    data.append(list(text))

operations = [x for x in lines[-1].split(" ") if x != '']

np_array = np.array(data)
groups, group = [], []
for i in range(len(np_array[0])):
    val = "".join(np_array[:, i])
    if (val.isspace()):
        groups.append(group)
        group = []
    else:
        group.append(val)
groups.append(group)  # Append last group

total = 0
for i, x in enumerate(operations):
    if (x == "+"):
        total += sum([int(k) for k in groups[i]])
    elif (x == "*"):
        total += np.prod([int(k) for k in groups[i]])

print("Total", total)

import numpy as np

file = open("input.txt")
lines = file.read().splitlines()

data = []
for text in lines[:-1]:
    data.append([int(x) for x in text.split(" ") if x != ''])

operations = [x for x in lines[-1].split(" ") if x != '']
np_array = np.array(data)

total = 0
for i, x in enumerate(operations):
    if (x == "+"):
        total += sum(np_array[:, i])  # Get column and sum
    elif (x == "*"):
        total += np.prod(np_array[:, i])  # Get column and sum

print("Total", total)

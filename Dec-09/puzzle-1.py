import itertools

file = open("input.txt")
lines = file.read().splitlines()

locations = []
for x in lines:
    locations.append([int(k) for k in x.split(",")])

pairs = itertools.combinations(locations, 2)

max_size = -1
for p1, p2 in list(pairs):
    x1, y1 = p1
    x2, y2 = p2
    size = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    if (size > max_size):
        max_size = size

print("Largest rectangle", max_size)

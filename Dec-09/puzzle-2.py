import itertools
from shapely.geometry.polygon import Polygon

file = open("input.txt")
lines = file.read().splitlines()

locations = []

for x in lines:
    cells = [int(k) for k in x.split(",")]
    cells.reverse()
    locations.append((cells[0], cells[1]))

polygon = Polygon((locations)).buffer(0.25)  # Create Polygon with given cells
pairs = itertools.combinations(locations, 2)

best = 0
for p1, p2 in pairs:
    x1, y1 = p1
    x2, y2 = p2

    new_pol = Polygon([(x1, y1), (x2, y2), (x2, y1), (x1, y2)])  # Create rectangle with 4 edges

    if polygon.covers(new_pol):
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height

        if area > best:
            best = area
            print("Valid rectangle:", p1, p2, "area =", area)

print("Largest rectangle", best)

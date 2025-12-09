import itertools

file = open("input.txt")
lines = file.read().splitlines()

locations = []

for x in lines:
    cells = [int(k) for k in x.split(",")]
    cells.reverse()
    locations.append((cells[0], cells[1]))

pairs = itertools.combinations(locations, 2)

# Capture all cells in the boundary
boundaries = []
for i in range(len(locations)):
    cx, cy = locations[i]
    nx, ny = locations[(i + 1) % len(locations)]

    if (cx == nx):
        boundaries.extend([(cx, y) for y in range(min(cy, ny), max(cy, ny) + 1)])
    elif (cy == ny):
        boundaries.extend([(x, cy) for x in range(min(cx, nx), max(cx, nx) + 1)])

boundaries = sorted(set(boundaries))

max_size = -1
for p1, p2 in pairs:
    x1, y1 = p1
    x2, y2 = p2
    size = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

    if (size <= max_size):
        continue

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # Check whether the rectangle contains any boundary cells which means rectangle flows out of the original polygon
    # Checking the rectangle contains in the shape(polygon) is difficult since the shape is complex
    crossed = False
    for bx, by in boundaries:
        if (min_x < bx < max_x and min_y < by < max_y):
            crossed = True
            break

    if (not crossed):
        if (size > max_size):
            print("Large", size)
            max_size = size

print("Largest rectangle", max_size)

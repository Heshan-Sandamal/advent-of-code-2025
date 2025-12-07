file = open("input.txt")
lines = file.read().splitlines()

grid, beams = [], []
for text in lines:
    grid.append(list(text))

for i, k in enumerate(grid[0]):
    if (k == "S"):
        beams.append((0, i))

splits = set()
while (len(beams) > 0):

    while (True):
        beam = beams.pop(0)
        x, y = beam[0] + 1, beam[1]

        if (x == len(grid)):
            break
        elif (grid[x][y] == "^"):
            splits.add((x, y))

            left, right = (x, y - 1), (x, y + 1)

            if (left[1] >= 0 and left not in beams):
                beams.append(left)

            if (right[1] < len(grid[0]) and right not in beams):
                beams.append(right)

            break
        else:
            beams.append((x, y))

print("Splits", len(splits))

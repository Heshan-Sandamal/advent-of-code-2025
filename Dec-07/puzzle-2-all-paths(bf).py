file = open("input.txt")
lines = file.read().splitlines()

grid, beams = [], []
for text in lines:
    grid.append(list(text))

for i, k in enumerate(grid[0]):
    if (k == "S"):
        beams.append((0, i))

# Find the all paths. Works for the smaller case because so many paths
# There are a lot of duplicate paths per splitter but this approach, we can not memorize paths
splits = 0
while (len(beams) > 0):

    while (True):
        beam = beams[0]
        x, y = beam[0] + 1, beam[1]

        if (x == len(grid)):
            beams.remove((beam))
            splits += 1
            break
        elif (grid[x][y] == "^"):
            beams.remove((beam))

            left, right = (x, y - 1), (x, y + 1)

            if (left[1] >= 0):
                beams.append(left)

            if (right[1] < len(grid[0])):
                beams.append(right)

            break
        else:
            beams[0] = (x, y)

print("Splits", splits)

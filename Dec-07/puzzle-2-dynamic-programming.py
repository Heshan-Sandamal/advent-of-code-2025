file = open("input.txt")
lines = file.read().splitlines()

# Had to rewrite the logic using dynamic programming pattern since brute force takes a lot of time
grid = []
for text in lines:
    grid.append(list(text))

# Create list of splitter locations
splitters = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if (grid[r][c] == "^"):
            splitters.append((r, c))
splitters.reverse()  # Start from bottom so that paths from splitter can be reused

# Keep track of paths per each splitter
manifolds_dic_paths = {}
for spt in splitters:
    x, y = spt[0], spt[1]
    left, right = (x, y - 1), (x, y + 1)

    beams = []  # Keep track of left and right beams starting from splitter
    if (left[1] >= 0):
        beams.append(left)

    if (right[1] < len(grid[0])):
        beams.append(right)

    count_per_splitter = 0
    while (len(beams) > 0):
        beam = beams[0]
        x, y = beam[0] + 1, beam[1]

        if (x == len(grid)):
            beams.remove((beam))
            count_per_splitter += 1
        elif (grid[x][y] == "^"):
            if ((x, y) in manifolds_dic_paths):
                count_per_splitter += manifolds_dic_paths[(x, y)]  # paths += paths from splitter
                beams.remove((beam))
            else:
                exit()  # Should not reach since path should be already calculated
        else:
            beams[0] = (x, y)

    manifolds_dic_paths[(spt[0], spt[1])] = count_per_splitter

print("Paths per splitter", manifolds_dic_paths)  # Answer is the paths from the top splitter

file = open("input.txt")
lines = file.read().splitlines()

grid = []
for text in lines:
    grid.append(list(text))


# Get Adjacent cell / neighbours of a cell in each direction
def get_adj_cells(r, c, rows, cols):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = []
    for x, y in directions:
        adj_x, adj_y = r + x, c + y
        if ((0 <= adj_x < rows) and (0 <= adj_y < cols)):
            neighbors.append((adj_x, adj_y))
    return neighbors


def get_adj_paper_count(adj_cells):
    adj_papers = 0
    for adj in adj_cells:
        adj_val = grid[adj[0]][adj[1]]
        if (adj_val == "@"):
            adj_papers += 1

        if (adj_papers >= 4):
            break

    return adj_papers


tot_papers = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        cell_val = grid[r][c]
        if (cell_val == "@"):
            adj_cells = get_adj_cells(r, c, len(grid), len(grid[0]))
            adj_papers_count = get_adj_paper_count(adj_cells)
            if (adj_papers_count < 4):
                tot_papers += 1

print("Total", tot_papers)

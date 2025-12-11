file = open("input.txt")
lines = file.read().splitlines()

start, end = "you", "out"
flow_dict = {}
for text in lines:
    key, flows = text.split(":")[0], list(text.split(":")[1].split(" ")[1:])
    flow_dict[key] = flows


def count_paths(node):
    if (node == end):
        return 1
    else:
        nodes = flow_dict[node]
        total = 0
        for x in nodes:
            total += count_paths(x)
        return total


print(count_paths(start))

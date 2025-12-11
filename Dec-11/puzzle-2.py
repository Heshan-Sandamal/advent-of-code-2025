file = open("input.txt")
lines = file.read().splitlines()

flow_dict = {}
for text in lines:
    key, flows = text.split(":")[0], list(text.split(":")[1].split(" ")[1:])
    flow_dict[key] = flows

memory = {}

start, end = "svr", "out"


def count_paths(node, paths, seen_fft, seen_dac):
    if node == "out":
        if (seen_fft and seen_dac):
            return 1
        else:
            return 0

    key = (node, seen_fft, seen_dac)

    if key in memory:
        return memory[key]

    total = 0
    if node in flow_dict:
        for nxt in flow_dict[node]:
            if nxt not in paths:
                total += count_paths(
                    nxt,
                    paths | {nxt},
                    seen_fft or nxt == "fft",
                    seen_dac or nxt == "dac"
                )

    memory[key] = total
    return total


print(count_paths(start, {start}, start == "fft", start == "dac"))

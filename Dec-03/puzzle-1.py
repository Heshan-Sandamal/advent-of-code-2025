file = open("input.txt")
lines = file.read().splitlines()

total = 0
for text in lines:
    batteries = list(text)
    max_v = max(batteries[:-1])

    max_index = batteries.index(max_v)
    second_max = max(batteries[max_index + 1:])

    total += int(max_v + second_max)

print("total", total)

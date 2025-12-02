import math

file = open("input.txt")
line = file.read().splitlines()[0]

ranges = line.split(",")

total = 0
for rng in ranges:
    start, end = int(rng.split("-")[0]), int(rng.split("-")[1])

    for x in range(start, end + 1):
        str_val = list(str(x))
        length = len(str_val)

        for k in range(1, math.ceil(length / 2) + 1):
            first = "".join(str_val[:k])

            if (first * int(length / k) == str(x) and x >= 11):
                total += x
                break

print("Total", total)

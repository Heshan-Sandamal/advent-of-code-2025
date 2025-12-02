file = open("input.txt")
line = file.read().splitlines()[0]

ranges = line.split(",")

total = 0
for rng in ranges:
    start, end = int(rng.split("-")[0]), int(rng.split("-")[1])

    for x in range(start, end + 1):
        str_val = list(str(x))

        first_half = str_val[:int(len(str_val) / 2)]
        second_half = str_val[int(len(str_val) / 2):]

        if (first_half == second_half):
            total += x


print("Total", total)

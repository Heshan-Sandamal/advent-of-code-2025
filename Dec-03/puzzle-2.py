file = open("input.txt")
lines = file.read().splitlines()

total = 0
for text in lines:
    batteries = list(text)

    digits = []
    for x in range(0, 12):
        max_v = max(batteries[:(len(batteries) - 11 + x)])
        digits.append(max_v)

        max_index = batteries.index(max_v)
        batteries = batteries[max_index + 1:]

    total += int("".join(digits))

print("total", total)

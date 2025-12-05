file = open("input.txt")
lines = file.read().splitlines()

ranges, boundaries = [], []
for text in lines:
    if (text == ""):
        break

    boundaries.append(int(text.split("-")[0]))
    boundaries.append(int(text.split("-")[1]))

    ranges.append(range(int(text.split("-")[0]), int(text.split("-")[1]) + 1))

sorted_all = (sorted(set(boundaries)))

start = sorted_all[0]
total = 1  # Keep track for total range starting with first inclusive
count_within_range = 0  # Keep track of within the existing range
x = min(sorted_all)

while (x <= max(sorted_all) + 1):
    in_range = False
    for r in ranges:
        if (x in r):
            total += (x - start)
            in_range = True
            count_within_range += 1

            # If count_within_range == 2,that means x is inside an existing range, hence we can move to end of the range
            if (count_within_range == 2):
                for t in sorted_all:
                    if (t >= x):
                        if (x != t):
                            total += (t - x)  # Increase the total by size of the range
                        x = t
                        count_within_range = 0
                        break

            start = x
            x += 1
            break

    if (not in_range):
        move_to_next_range = False
        for t in sorted_all:
            if (t >= x):
                x = t
                start = t
                move_to_next_range = True
                total += 1  # Starting point is inclusive
                break

        if (not move_to_next_range):
            x += 1


print(total)

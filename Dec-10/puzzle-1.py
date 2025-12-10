import itertools

file = open("input.txt")
lines = file.read().splitlines()

total = []
for line in lines:
    line_d = line.split(" ")
    diagram = list(line_d[0])[1:-1]
    buttons = []
    for k in line_d[1:-1]:
        buttons.append([(int(g)) for g in k[1:-1].split(",")])

    # No multiple presses of single button needed hence checking combinations of buttons
    min_p = 100000000000000000000000000
    for x in range(1, len(buttons)):
        pairs = itertools.combinations(buttons, x)

        for p in pairs:
            start = ["." for t in range(len(diagram))]
            for p_array in p:
                for i in p_array:
                    if (start[i] == "."):
                        start[i] = "#"
                    elif (start[i] == "#"):
                        start[i] = "."

            if (start == diagram):
                if (x < min_p):
                    min_p = x
                print("Presses", start, x, p)
                break

    total.append(min_p)

print("Min presses", sum(total))

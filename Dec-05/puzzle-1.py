file = open("input.txt")
lines = file.read().splitlines()

ranges, ingredients = [], []
ranges_input = True

for text in lines:
    if (text == ""):
        ranges_input = False
        continue

    if (ranges_input):
        ranges.append(range(int(text.split("-")[0]), int(text.split("-")[1]) + 1))
    else:
        ingredients.append(int(text))

total = 0
for ing in ingredients:
    for rng in ranges:
        if (ing in rng):
            total += 1
            break

print("Fresh available", total)

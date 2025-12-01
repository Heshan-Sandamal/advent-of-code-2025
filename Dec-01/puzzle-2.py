import math

file = open("input.txt")
lines = file.read().splitlines()

start = 50
password = 0
for text in lines:
    direction, value = text[0], int(text[1:])

    if ("R" == direction):
        rem = (value % 100)
        if ((start + rem) > 99):
            password += 1  # Capture whether the remainder + start goes beyond 100

        password += math.floor(value / 100)  # Capture cycles

        start = (start + value) % 100

    elif ("L" == direction):
        rem = (value % 100)
        if (start != 0 and (start - rem) <= 0):
            password += 1  # Capture whether the start - remainder is less than 0

        password += math.floor(value / 100)
        start = (start - value) % 100

print("Password", password)

import math

file = open("input.txt")
lines = file.read().splitlines()

start, start_n = 50, 0
password = 0
for text in lines:
    direction, value = text[0], int(text[1:])
    if ("R" == direction):
        rot = (value % 100)
        if (start + rot > 99):
            password += 1
        password += math.floor(value / 100)
        start = (start + value) % 100

    elif ("L" == direction):
        rot = (value % 100)
        if (start != 0 and start - rot <= 0):
            password += 1

        password += math.floor(value / 100)
        start = (start - value) % 100

print("Password", password)

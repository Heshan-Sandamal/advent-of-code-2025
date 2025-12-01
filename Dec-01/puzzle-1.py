file = open("input.txt")
lines = file.read().splitlines()

start = 50
password = 0
for text in lines:
    direction, value = text[0], int(text[1:])
    if ("R" == direction):
        start = (start + value) % 100
    elif ("L" == direction):
        start = (start - value) % 100

    if (start == 0):
        password += 1

print("Password", password)

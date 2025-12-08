import itertools
import math

file = open("input.txt")
lines = file.read().splitlines()


# Calculate Distance
def distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2 + (loc1[2] - loc2[2]) ** 2)


junctions = []
for text in lines:
    locs = text.split(",")
    junctions.append((int(locs[0]), int(locs[1]), int(locs[2])))

# Get all pair combinations
pairs = itertools.combinations(junctions, 2)

# Sort by distance
sorted_pairs = sorted(
    pairs,
    key=lambda pair: distance(pair[0], pair[1])
)

# Keep track of groups
groups = [[sorted_pairs[0][0], sorted_pairs[0][1]]]

for pair in sorted_pairs:
    exists = False
    existing_group = None
    for i, group in enumerate(groups):
        if ((pair[0] in group or pair[1] in group)):
            if (not exists):
                exists = True
                group.extend([pair[0], pair[1]])
                existing_group = group
            else:
                # If one of the items in pair exists in a previous group, extend first group and delete others
                existing_group.extend(group)
                del groups[i]

    if (not exists):
        groups.append([pair[0], pair[1]])

    if (len(set(groups[0])) == len(junctions)):
        print("Answer:", pair[0][0] * pair[1][0])
        break

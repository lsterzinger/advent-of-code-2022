# Open input file
with open('input', 'r') as f:
    food = f.readlines()

# Sum for each elf
elftot = 0
elfs = []

for line in food:
    l = line.strip()
    if l == '':
        elfs.append(elftot)
        elftot = 0
    else:
        elftot += int(l)

print("The max carried by an elf is ", max(elfs))

print("The sum of the top 3 elves is ", sum(sorted(elfs)[-3:]))

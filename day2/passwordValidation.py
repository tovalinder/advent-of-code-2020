
def part1(pwds): 
    validCount = 0
    for line in pwds: 
        comp = (line.split(' '))
        limits = comp[0].split("-")
        low = int(limits[0])
        high = int(limits[1])
        letter = comp[1][:-1]
        pw = comp[2][:-1]
        occurances = pw.count(letter)
        if (occurances >= low and occurances <= high):
            validCount += 1

    return validCount

def part2(pwds):
    validCount = 0
    for line in pwds: 
        comp = (line.split(' '))
        positions = comp[0].split("-")
        firstPos = int(positions[0])
        secondPos = int(positions[1])
        letter = comp[1][:-1]
        pw = comp[2][:-1]

        oneIs = pw[firstPos-1] == letter or pw[secondPos-1] == letter 
        bothAre = pw[firstPos-1] == letter and pw[secondPos-1] == letter

        if oneIs and not bothAre:
            validCount += 1

    return validCount

with open("../data/day2.txt") as f:
    pwds = f.readlines()
    print(part1(pwds))
    print(part2(pwds))             



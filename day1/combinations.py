import itertools


def part1(content):
    combinations = itertools.combinations(content, 2)
    for combination in combinations:
        sum = int(combination[0]) + int(combination[1])
        if sum == 2020:
            print(int(combination[0]) * int(combination[1]))

def part2(content):
    combinations = itertools.combinations(content, 3)
    for combination in combinations:
        sum = int(combination[0]) + int(combination[1]) + int(combination[2])
        if sum == 2020:
            print(int(combination[0]) * int(combination[1]) * int(combination[2]))
            
with open("../data/day1.txt") as f: 
    content = f.readlines()
    part1(content)
    part2(content)
    
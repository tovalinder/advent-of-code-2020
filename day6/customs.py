def part1(groups):
    joint_groups = [set(group.replace("\n", "")) for group in groups]
    print(sum(map(len, joint_groups)))

def part2(groups):
    splitted_groups = [map(set, group.splitlines()) for group in groups]
    intersections = [set.intersection(*s) for s in splitted_groups]
    print(sum(map(len, intersections)))

with open("../data/day6.txt") as f:
    declarations = f.read()
    groups = declarations.split('\n\n')
    part1(groups)
    part2(groups)
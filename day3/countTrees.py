import numpy

def countTrees(forest, slope): 
    row = 0
    col = 0
    trees = 0
    while row < rows - 1:
        col = (col + slope[0]) % cols
        row += slope[1]
        if forest[row][col] == '#': 
            trees += 1
    return trees

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

with open("../data/day3.txt") as f: 
    forest = f.read().splitlines() 
    cols = len(forest[0])
    rows = len(forest)

    trees = []
    for slope in slopes:
        trees.append(countTrees(forest, slope))

    print(trees)
    print(numpy.prod(trees))
    



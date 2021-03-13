import networkx as nx  

def createRuleGraph(rules):
    graph = nx.DiGraph()
    for rule in rules:
        rootAndRest = rule.replace('bags', '').replace('bag', '').split('contain')
        root = rootAndRest.pop(0).strip().replace(' ', '-') 
        neighbors = rootAndRest.pop(0).replace('.', '').split(',')
        for neighbor in neighbors: 
            split = neighbor.strip().split(' ')
            if len(split) == 3:
                graph.add_edge(root, split[1] + '-' + split[2], weight=split[0])
    return graph

def part1(graph): 
    print(len(nx.ancestors(graph, 'shiny-gold')))

def part2(graph):
    def rec_count(node):
        bag_count = 1
        for neighbor in nx.neighbors(graph, node):
            bag_count += rec_count(neighbor) * int(graph[node][neighbor]['weight'])
        return bag_count
    
    print(rec_count('shiny-gold') - 1)

with open("../data/day7.txt") as f:
    rules = f.readlines()
    graph = createRuleGraph(rules)
    part1(graph)
    part2(graph)


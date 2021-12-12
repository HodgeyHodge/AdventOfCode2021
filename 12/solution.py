
filename = "testinput1.txt"
edges = []
nodes = set()

with open(filename) as file:
    for line in file:
        a, b = line.strip('\n').split('-')
        edges.append((a, b))
        edges.append((b, a))
        nodes.add(a)
        nodes.add(b)

paths = [['start']]

final_paths = []
while len(paths) > 0:
    continued_paths = []
    for path in paths:
        if path[-1] == 'end':
            final_paths.append(path)
            continue
        for new_node in (edge[1] for edge in edges if edge[0] == path[-1]):
            if not any([new_node == node for node in path if new_node == new_node.lower()]):
                continued_paths.append(path[:] + [new_node])
    paths = continued_paths

print(len(final_paths))





    

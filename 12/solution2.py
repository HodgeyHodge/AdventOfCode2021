
filename = "input.txt"
edges = []
nodes = set()

with open(filename) as file:
    for line in file:
        a, b = line.strip('\n').split('-')
        edges.append((a, b))
        edges.append((b, a))
        nodes.add(a)
        nodes.add(b)

paths = [(['start'], False)]

final_paths = []
while len(paths) > 0:
    continued_paths = []
    for path in paths:
        if path[0][-1] == 'end':
            final_paths.append(path)
            continue
        for new_node in (edge[1] for edge in edges if edge[0] == path[0][-1] and edge[1] != 'start'):
            if not path[1]:
                continued_path = (path[0][:] + [new_node], any([new_node == node for node in path[0] if node == node.lower()]))
                continued_paths.append(continued_path)
            else:
                if not any([new_node == node for node in path[0] if node == node.lower()]):
                    continued_path = (path[0][:] + [new_node], True)
                    continued_paths.append(continued_path)
    paths = continued_paths

print(len(final_paths))


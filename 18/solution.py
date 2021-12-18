
from math import floor, ceil
from ast import literal_eval

class Tree:
    def __init__(self, init):
        if init is None:
            self.data = None
            self.left = None
            self.right = None
        elif type(init) is int:
            self.data = init
            self.left = None
            self.right = None
        elif type(init) is list:
            self.data = None
            self.left = Tree(init[0])
            self.right = Tree(init[1])
        elif type(init) is Tree:
            self.data = None
            self.left = init.left
            self.right = init.right
        
    def __str__(self):
        return str(self.listify())

    def clone(self):
        new = Tree(self.data)
        if self.left:
            new.left = self.left.clone()
        if self.right:
            new.right = self.right.clone()
        return new
    
    def __add__(self, other):
        n = Tree([self.clone(), other.clone()])
        return n.reduce()
    
    def listify(self):
        if self.data is not None:
            return self.data
        else:
            return [self.left.listify(), self.right.listify()]

    def __iter__(self):
        yield self
        if self.left:
            for node in self.left:
                yield node
        if self.right:
            for node in self.right:
                yield node

    def iterate_with_depth(self, level = 0):
        yield self, level
        if self.left:
            for node, level in self.left.iterate_with_depth():
                yield node, level + 1
        if self.right:
            for node, level in self.right.iterate_with_depth():
                yield node, level + 1

    def split(self):
        for node, level in self.iterate_with_depth():
            if node.data is not None and node.data >= 10:
                node.left = Tree(floor(node.data / 2))
                node.right = Tree(ceil(node.data / 2))
                node.data = None
                return True
        return False

    def add_left(self, n):
        if self.data is not None:
            self.data += n
        else:
            self.left.add_left(n)

    def add_right(self, n):
        if self.data is not None:
            self.data += n
        else:
            self.right.add_right(n)

    def explode(self):
        prev_node = None
        prev_level = None
        this_node = None
        this_level = None
        next_node = None
        next_level = None
        for node, level in self.iterate_with_depth():
            if level == 4 or (level < 4 and node.data is not None):
                prev_node = this_node
                prev_level = this_level
                this_node = next_node
                this_level = next_level
                next_node = node
                next_level = level
                if this_level == 4 and this_node.data is None:
                    if prev_node:
                        prev_node.add_right(this_node.left.data)
                    if next_node:
                        next_node.add_left(this_node.right.data)
                    this_node.left = None
                    this_node.right = None
                    this_node.data = 0
                    return True
        #one more iteration to force check of rightmost node:
        prev_node = this_node
        prev_level = this_level
        this_node = next_node
        this_level = next_level
        next_node = None
        next_level = 0
        if this_level == 4 and this_node.data is None:
            if prev_node:
                prev_node.add_right(this_node.left.data)
            if next_node:
                next_node.add_left(this_node.right.data)
            this_node.left = None
            this_node.right = None
            this_node.data = 0
            return True
        return False
    
    def reduce(self):
        while True:
            if self.explode():
                continue
            if self.split():
                continue
            break
        return self

    def magnitude(self):
        if self.data is not None:
            return self.data
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()



assert(Tree([[1,2],[[3,4],5]]).magnitude() == 143)
assert(Tree([[[[0,7],4],[[7,8],[6,0]]],[8,1]] ).magnitude() ==  1384)
assert(Tree([[[[1,1],[2,2]],[3,3]],[4,4]] ).magnitude() ==  445)
assert(Tree([[[[3,0],[5,3]],[4,4]],[5,5]] ).magnitude() ==  791)
assert(Tree([[[[5,0],[7,4]],[5,5]],[6,6]] ).magnitude() ==  1137)
assert(Tree([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] ).magnitude() ==  3488)

t = None
for a in [
    [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
    [[[5,[2,8]],4],[5,[[9,9],0]]],
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
    [[[[5,4],[7,7]],8],[[8,3],8]],
    [[9,3],[[9,9],[6,[4,9]]]],
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
]:
    if t is None:
        t = Tree(a)
    else:
        t += Tree(a)
assert(t.magnitude() == 4140)

with open("input.txt") as file:
    numbers = [Tree(literal_eval(line.strip('\n'))) for line in file]

t = None
for a in numbers:
    if t is None:
        t = a
    else:
        t += a
print('part one:', t.magnitude())

numbers = [
    [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
    [[[5,[2,8]],4],[5,[[9,9],0]]],
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
    [[[[5,4],[7,7]],8],[[8,3],8]],
    [[9,3],[[9,9],[6,[4,9]]]],
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
]
max_magnitude = 0
for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        if i != j:
            max_magnitude = max(max_magnitude, (Tree(numbers[i]) + Tree(numbers[j])).magnitude())
assert(max_magnitude == 3993)

with open("input.txt") as file:
    numbers = [Tree(literal_eval(line.strip('\n'))) for line in file]
max_magnitude = 0
for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        if i != j:
            sum_tree = numbers[i] + numbers[j]
            current_magnitude = sum_tree.magnitude()
            if current_magnitude > max_magnitude:
                max_magnitude = current_magnitude
print('part two:', max_magnitude)











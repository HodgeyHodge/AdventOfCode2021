
def subtract_points(x, y):
    return tuple(a - b for a, b in zip(x, y))

def add_points(x, y):
    return tuple(a + b for a, b in zip(x, y))

def points_equal(x, y):
    return all(a == b for a, b in zip(x, y))

def realign(x, y, z, i):
    # there are actually 48 of these but the problem excludes the determinant -1 rotations
    if i == 0: return x, y, z
    if i == 1: return x, y, -z 
    if i == 2: return x, -y, z
    if i == 3: return x, -y, -z
    if i == 4: return -x, y, z
    if i == 5: return -x, y, -z
    if i == 6: return -x, -y, z
    if i == 7: return -x, -y, -z
    if i == 8: return z, x, y
    if i == 9: return z, x, -y
    if i == 10: return z, -x, y
    if i == 11: return z, -x, -y
    if i == 12: return -z, x, y
    if i == 13: return -z, x, -y
    if i == 14: return -z, -x, y
    if i == 15: return -z, -x, -y
    if i == 16: return y, z, x
    if i == 17: return y, z, -x
    if i == 18: return y, -z, x
    if i == 19: return y, -z, -x
    if i == 20: return -y, z, x
    if i == 21: return -y, z, -x
    if i == 22: return -y, -z, x
    if i == 23: return -y, -z, -x
    if i == 24: return x, z, y
    if i == 25: return x, z, -y
    if i == 26: return x, -z, y
    if i == 27: return x, -z, -y
    if i == 28: return -x, z, y
    if i == 29: return -x, z, -y
    if i == 30: return -x, -z, y
    if i == 31: return -x, -z, -y
    if i == 32: return y, x, z
    if i == 33: return y, x, -z
    if i == 34: return y, -x, z
    if i == 35: return y, -x, -z
    if i == 36: return -y, x, z
    if i == 37: return -y, x, -z
    if i == 38: return -y, -x, z
    if i == 39: return -y, -x, -z
    if i == 40: return z, y, x
    if i == 41: return z, y, -x
    if i == 42: return z, -y, x
    if i == 43: return z, -y, -x
    if i == 44: return -z, y, x
    if i == 45: return -z, y, -x
    if i == 46: return -z, -y, x
    if i == 47: return -z, -y, -x

def reverse_realign(x, y, z, i):
    # there are actually 48 of these but the problem excludes the determinant -1 rotations
    if i == 0: return x, y, z # x, y, z
    if i == 1: return x, y, -z # x, y, -z 
    if i == 2: return x, -y, z # x, -y, z
    if i == 3: return x, -y, -z # x, -y, -z
    if i == 4: return -x, y, z # -x, y, z
    if i == 5: return -x, y, -z # -x, y, -z
    if i == 6: return -x, -y, z # -x, -y, z
    if i == 7: return -x, -y, -z # -x, -y, -z
    if i == 8: return y, z, x # z, x, y
    if i == 9: return y, -z, x # z, x, -y
    if i == 10: return -y, z, x # z, -x, y
    if i == 11: return -y, -z, x # z, -x, -y
    if i == 12: return y, z, -x # -z, x, y
    if i == 13: return y, -z, -x # -z, x, -y
    if i == 14: return -y, z, -x # -z, -x, y
    if i == 15: return -y, -z, -x # -z, -x, -y
    if i == 16: return z, x, y # y, z, x
    if i == 17: return -z, x, y # y, z, -x
    if i == 18: return z, x, -y # y, -z, x
    if i == 19: return -z, x, -y # y, -z, -x
    if i == 20: return z, -x, y # -y, z, x
    if i == 21: return -z, -x, y # -y, z, -x
    if i == 22: return z, -x, -y # -y, -z, x
    if i == 23: return -z, -x, -y # -y, -z, -x
    if i == 24: return x, z, y # x, z, y
    if i == 25: return x, -z, y # x, z, -y
    if i == 26: return x, z, -y # x, -z, y
    if i == 27: return x, -z, -y # x, -z, -y
    if i == 28: return -x, z, y # -x, z, y
    if i == 29: return -x, -z, y # -x, z, -y
    if i == 30: return -x, z, -y # -x, -z, y
    if i == 31: return -x, -z, -y # -x, -z, -y
    if i == 32: return y, x, z # y, x, z
    if i == 33: return y, x, -z # y, x, -z
    if i == 34: return -y, x, z # y, -x, z
    if i == 35: return -y, x, -z # y, -x, -z
    if i == 36: return y, -x, z # -y, x, z
    if i == 37: return y, -x, -z # -y, x, -z
    if i == 38: return -y, -x, z # -y, -x, z
    if i == 39: return -y, -x, -z # -y, -x, -z
    if i == 40: return z, y, x # z, y, x
    if i == 41: return -z, y, x # z, y, -x
    if i == 42: return z, -y, x # z, -y, x
    if i == 43: return -z, -y, x # z, -y, -x
    if i == 44: return z, y, -x # -z, y, x
    if i == 45: return -z, y, -x # -z, y, -x
    if i == 46: return z, -y, -x # -z, -y, x
    if i == 47: return -z, -y, -x # -z, -y, -x

def spell(p, c, d):
    #take a point p and return its respelling through c, d
    return subtract_points(realign(*p, c), d)

def despell(q, c, d):
    #take a point q that has been respelled through c, d, and return the original
    return reverse_realign(*add_points(q, d), c)
 
def load_file(filename):
    scanner_output = {0: set()}
    i = 0
    with open(filename) as file:
        for line in file.readlines():
            if line == '\n':
                i += 1
                scanner_output[i] = set()
            elif line.startswith('---'):
                continue
            else:
                scanner_output[i].add(tuple(int(x) for x in line.strip('\n').split(',')))
    return scanner_output

def check_overlap(i, j):
    for p in scanner_output[i]:
        for q in scanner_output[j]:
            for c in range(0, 48):
                q_ = realign(*q, c)
                d = subtract_points(q_, p)
                count = 0
                for r in scanner_output[j]:
                    if not points_equal(r, q):
                        if spell(r, c, d) in scanner_output[i]:
                            count += 1
                            if count == 11:
                                return True, c, d
    return False, 0, 0



assert(subtract_points((1, 2), (3, 5))[0] == -2)
assert(subtract_points((1, 2), (3, 5))[1] == -3)

assert(add_points((1, 2), (3, 5))[0] == 4)
assert(add_points((1, 2), (3, 5))[1] == 7)

assert(points_equal((1, 2), (1, 2)))
assert(not points_equal((1, 2), (1, 3)))
assert(not points_equal((1, 2), (2, 2)))

for i in range(0, 48):
    assert(despell(spell((1, 2, 3), i, (10, 20, 30)), i, (10, 20, 30)) == (1, 2, 3))



scanner_output = load_file('input.txt')
beacons = set()
spellings = set()
scanners = set()

print('Adding beacons from all scanners in their own spellings')
for scanner in scanner_output:
    for beacon in scanner_output[scanner]:
        beacons.add((beacon, scanner))

for i in scanner_output:
    for j in scanner_output:
        if i > j:
            print(f'Checking for overlap between scanners {i} and {j}')
            v, c, d = check_overlap(i, j)
            if v:
                print(f'Found an overlap between scanners {i} and {j} at alignment {c}, offset {d}')
                
                print(f'Recording beacons from scanner {i}')
                for p in scanner_output[i]:
                    beacons.add((p, i))
                    beacons
                    
                print(f'Recording beacons from scanner {j}')
                for q in scanner_output[j]:
                    beacons.add((q, j))
                
                print(f'Recording spelling {i} <- {j}: {c} {d}')
                spellings.add((i, j, c, d))

# to satisfy part one:

lengths = []
while True:
    new_beacons = []
    for b in beacons:
        for s in spellings:
            if s[0] == b[1]:
                new_beacons.append((despell(b[0], s[2], s[3]), s[1]))
            elif s[1] == b[1]:
                new_beacons.append((spell(b[0], s[2], s[3]), s[0]))
    beacons.update(new_beacons)
    new_lengths = [len([beacon for beacon in beacons if beacon[1] == i]) for i in scanner_output]
    if lengths == new_lengths:
        print(lengths)
        break
    lengths = new_lengths

# to satisfy part two:

scanners = set([((0, 0, 0), i) for i in scanner_output])
lengths = [] 
while True:
    new_scanners = []
    for x in scanners:
        for s in spellings:
            if s[0] == x[1]:
                new_scanners.append((despell(x[0], s[2], s[3]), s[1]))
            elif s[1] == x[1]:
                new_scanners.append((spell(x[0], s[2], s[3]), s[0]))
    scanners.update(new_scanners)
    new_lengths = [len([scanner for scanner in scanners if scanner[1] == i]) for i in scanner_output]
    if lengths == new_lengths:
        print(lengths)
        break
    lengths = new_lengths
                
max_dist = 0
for p in [scanner for scanner in scanners if scanner[1] == 0]:
    for q in [scanner for scanner in scanners if scanner[1] == 0]:
        max_dist = max(max_dist, sum(abs(dist) for dist in subtract_points(p[0], q[0])))

print(max_dist)





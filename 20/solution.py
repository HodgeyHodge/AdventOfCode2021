
def load_file(filename):
    pixels = set()
    with open(filename) as file:
        i = 0
        for line in file:
            j = 0
            for pixel in line.strip('\n'):
                if pixel == '#':
                    pixels.add((i, j))
                j += 1
            i += 1
    return pixels

def get_pixel_number(pixels, i, j, bounds, backlit):
    if backlit:
        output = (1 if (i + 1, j + 1) in pixels or (i + 1 > bounds[1] or j + 1 > bounds[3]) else 0) \
            + (2 if (i + 1, j) in pixels or (i + 1 > bounds[1] or j < bounds[2] or j > bounds[3]) else 0) \
            + (4 if (i + 1, j - 1) in pixels or (i + 1 > bounds[1] or j - 1 < bounds[2]) else 0) \
            + (8 if (i, j + 1) in pixels or (i < bounds[0] or i > bounds[1] or j + 1 > bounds[3]) else 0) \
            + (16 if (i, j) in pixels or (i < bounds[0] or i > bounds[1] or j < bounds[2] or j > bounds[3]) else 0) \
            + (32 if (i, j - 1) in pixels or (i < bounds[0] or i > bounds[1] or j - 1 < bounds[2])else 0) \
            + (64 if (i - 1, j + 1) in pixels or (i - 1 < bounds[0] or j + 1 > bounds[3]) else 0) \
            + (128 if (i - 1, j) in pixels or (i - 1 < bounds[0] or j < bounds[2] or j > bounds[3]) else 0) \
            + (256 if (i - 1, j - 1) in pixels or (i - 1 < bounds[0] or j - 1 < bounds[2]) else 0)
    else:
        output = (1 if (i + 1, j + 1) in pixels else 0) \
            + (2 if (i + 1, j) in pixels else 0) \
            + (4 if (i + 1, j - 1) in pixels else 0) \
            + (8 if (i, j + 1) in pixels else 0 )\
            + (16 if (i, j) in pixels else 0) \
            + (32 if (i, j - 1) in pixels else 0) \
            + (64 if (i - 1, j + 1) in pixels else 0) \
            + (128 if (i - 1, j) in pixels else 0) \
            + (256 if (i - 1, j - 1) in pixels else 0)
    return output

assert(get_pixel_number(set([(0, 0)]), 1, 1, None, False) == 256)
assert(get_pixel_number(set([(0, 1)]), 1, 1, None, False) == 128)
assert(get_pixel_number(set([(0, 2)]), 1, 1, None, False) == 64)
assert(get_pixel_number(set([(1, 0)]), 1, 1, None, False) == 32)
assert(get_pixel_number(set([(1, 1)]), 1, 1, None, False) == 16)
assert(get_pixel_number(set([(1, 2)]), 1, 1, None, False) == 8)
assert(get_pixel_number(set([(2, 0)]), 1, 1, None, False) == 4)
assert(get_pixel_number(set([(2, 1)]), 1, 1, None, False) == 2)
assert(get_pixel_number(set([(2, 2)]), 1, 1, None, False) == 1)

assert(get_pixel_number(set(), 1, 1, (0, 2, 0, 2), True) == 0)

assert(get_pixel_number(set(), 0, 0, (0, 2, 0, 2), True) == 484) # 4 + 32 + 64 + 128 + 256
assert(get_pixel_number(set(), 0, 1, (0, 2, 0, 2), True) == 448) # 64 + 128 + 256
assert(get_pixel_number(set(), 0, 2, (0, 2, 0, 2), True) == 457) # 1 + 8 + 64 + 128 + 256
assert(get_pixel_number(set(), 1, 2, (0, 2, 0, 2), True) == 73) # 1 + 8 + 64
assert(get_pixel_number(set(), 2, 2, (0, 2, 0, 2), True) == 79) # 1 + 2 + 4 + 8 + 64
assert(get_pixel_number(set(), 2, 1, (0, 2, 0, 2), True) == 7) # 1 + 2 + 4
assert(get_pixel_number(set(), 2, 0, (0, 2, 0, 2), True) == 295) # 1 + 2 + 4 + 32 + 256
assert(get_pixel_number(set(), 1, 0, (0, 2, 0, 2), True) == 292) # 4 + 32 + 256

def get_bounds(pixels):
    return (min([p[0] for p in pixels]), max([p[0] for p in pixels]), min([p[1] for p in pixels]), max([p[1] for p in pixels]))

def enhance(pixels, enhancer, backlit):
    bounds = get_bounds(pixels)
    new_pixels = set()
    for i in range (bounds[0] - 1, bounds[1] + 2):
        for j in range(bounds[2] - 1, bounds[3] + 2):
            if enhancer[get_pixel_number(pixels, i, j, bounds, backlit)] == '#':
                new_pixels.add((i, j))
    return new_pixels

def pretty_print(pixels, backlit):
    bounds = get_bounds(pixels)

    new_pixels = set()
    new_pixels.update(pixels)
    
    if backlit:
        for i in range(bounds[0] - 2, bounds[1] + 3):
            new_pixels.add((i, bounds[2] - 1))
            new_pixels.add((i, bounds[2] - 2))
            new_pixels.add((i, bounds[3] + 1))
            new_pixels.add((i, bounds[3] + 2))
        for j in range(bounds[2] - 2, bounds[3] + 3):
            new_pixels.add((bounds[0] - 1, j))
            new_pixels.add((bounds[0] - 2, j))
            new_pixels.add((bounds[1] + 1, j))
            new_pixels.add((bounds[1] + 2, j))

    for i in range (bounds[0] - 2, bounds[1] + 3):
        for j in range(bounds[2] - 2, bounds[3] + 3):
            print('#' if (i, j) in new_pixels else '.', end='')
        print('')
    print('')

def iterate(pixels, enhancer, n):
    oscillating = (enhancer[0] == '#')
    backlit = False
    #pretty_print(pixels, backlit)
    #print(len(pixels))
    for i in range(0, n):
        pixels = enhance(pixels, enhancer, backlit)
        if oscillating:
            backlit = not backlit
    #pretty_print(pixels, backlit)
    print(len(pixels))

live_enhancer = '##..####..###.#.#.#.#..######.#..#....##....###.........###....###.#########.#####..##..#.#.#..###..#..##.##...###.###.#.##.####..#.##.#.##.##.##.####....#.##...##.####.#...........#.#..#.##..#....#.###.###.#.##.#..###.#...#.#.....#####.####.####.##...#.#....#.#.#.###.#.##.##.#.####..#####.##..#.#.#..#....##..#.###....#..#.###...#...#...##.......#.#..#..#.#....#..#.#.###.##....#..#..##.#..###...#.######..#.##..#.#.#.###.###..##.#......#.#.##.....##..#.###.#.##..#.###########.......###.#..#..####...#.#.#.##.'
test_enhancer = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'

iterate(load_file('testinput.txt'), test_enhancer, 50)
iterate(load_file('input.txt'), live_enhancer, 50)








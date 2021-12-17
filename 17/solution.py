
from math import sqrt, floor

def fire(v, w, F, R, B, T):
    x, y = 0, 0
    while x <= R and y >= B:
        if x >= F and y <= T:
            return True
        x += v
        y += w
        if v > 0:
            v -= 1
        w -= 1
    return False

def find_highest_trajectory_shot(F, R, T, B):
    best_w = B
    for v in range(floor(0.5 * sqrt(8 * F + 1) - 0.5), R + 1):
        for w in range(B, -B + 1):
            if fire(v, w, F, R, B, T):
                if w > best_w:
                    best_w = w
    return int(0.5 * best_w * (best_w + 1))

def find_all_shots(F, R, T, B):
    num_shots = 0
    for v in range(floor(0.5 * sqrt(8 * F + 1) - 0.5), R + 1):
        for w in range(B, -B + 1):
            if fire(v, w, F, R, B, T):
                num_shots += 1
    return num_shots

# part one:

print(find_highest_trajectory_shot(20, 30, -5, -10))
print(find_highest_trajectory_shot(179, 201, -63, -109))

# part two:

print(find_all_shots(20, 30, -5, -10))
print(find_all_shots(179, 201, -63, -109))








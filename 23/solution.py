from random import choice

def hallway_clear(H, a, b):
    return not any(h_ for h_ in H[min(a, b) : max(a, b) + 1])

def path_home_clear(H, r, h):
    if r < h:
        return hallway_clear(H, r, h - 1)
    else:
        return hallway_clear(H, h + 1, r)

def home(r, x):
    if r == 2:
        return x == 'A'
    elif r == 4:
        return x == 'B'
    elif r == 6:
        return x == 'C'
    elif r == 8:
        return x == 'D'

def done(R):
    return \
        R[2] == 'AAAA' and \
        R[4] == 'BBBB' and \
        R[6] == 'CCCC' and \
        R[8] == 'DDDD'

def entry_only(room, r):
    if r == 2:
        return 'B' not in room and 'C' not in room and 'D' not in room
    elif r == 4:
        return 'A' not in room and 'C' not in room and 'D' not in room
    elif r == 6:
        return 'A' not in room and 'B' not in room and 'D' not in room
    elif r == 8:
        return 'A' not in room and 'B' not in room and 'C' not in room

def power(x):
    if x == 'A':
        return 1
    elif x == 'B':
        return 10
    elif x == 'C':
        return 100
    elif x == 'D':
        return 1000

def get_valid_moves(game):
    moves = []
    R = game[0]
    H = game[1]
    for r in [2, 4, 6, 8]:
        if R[r] and not entry_only(R[r], r):
            for h in [0, 1, 3, 5, 7, 9, 10]:
                if hallway_clear(H, r, h):
                    moves.append((0, r, h, (5 - len(R[r]) + abs(r - h)) * power(R[r][-1])))
    for h in [0, 1, 3, 5, 7, 9, 10]:
        if H[h]:
            for r in [2, 4, 6, 8]:
                if entry_only(R[r], r) and home(r, H[h]) and path_home_clear(H, r, h):
                    moves.append((1, r, h, (4 - len(R[r]) + abs(r - h)) * power(H[h])))
    return moves

def apply_move(move, R, H):
    r = move[1]
    h = move[2]
    if move[0] == 0:
        H[h] = R[r][-1]
        R[r] = R[r][0:-1]
    else:
        R[r] += H[h]
        H[h] = ''

def run(rooms, hallway):
    games = [(rooms, hallway, 0)]
    ply = 0
    min_cost = 0
    
    while True:
        next_games = []
        for game in games:
            #print(f'After {ply} moves, considering game: {game}')
            moves = get_valid_moves(game)
            #print(f'Valid moves are: {moves}')
            if len(moves) == 0:
                if done(game[0]):
                    #print(f'final cost: {game[2]}')
                    if min_cost == 0:
                        min_cost = game[2]
                    else:
                        min_cost = min(min_cost, game[2])
            if any([move[0] == 1 for move in moves]):
                for move in moves:
                    if move[0] == 1:
                        next_rooms = game[0][:]
                        next_hallway = game[1][:]
                        #print(f'Applying move {move} to {next_rooms} / {next_hallway}...')
                        apply_move(move, next_rooms, next_hallway)
                        #print(f'...bam! {next_rooms} / {next_hallway}...')
                        next_games.append((next_rooms, next_hallway, game[2] + move[3]))
            else:
                for move in moves:
                    next_rooms = game[0][:]
                    next_hallway = game[1][:]
                    #print(f'Applying move {move} to {next_rooms} / {next_hallway}...')
                    apply_move(move, next_rooms, next_hallway)
                    #print(f'...bam! {next_rooms} / {next_hallway}...')
                    next_games.append((next_rooms, next_hallway, game[2] + move[3]))
        games = next_games[:]
        ply += 1
        print(ply, len(games))
        if len(games) == 0:
            print(min_cost)
            break

rooms = [None, None, 'CDDA', None, 'DBCD', None, 'BABA', None, 'BCAC', None, None]
hallway = ['', '', None, '', None, '', None, '', None, '', '']

run(rooms, hallway)











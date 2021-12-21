
def new_position(position, roll, board_size):
    return (position + roll - 1) % board_size + 1

def build_player_history(start_position, board_size, die_size, points_to_win):
    state_history = [{(start_position, 0): 1}]

    while True:
        new_gamestates = {}
        for i in range(1, die_size + 1):
            for j in range(1, die_size + 1):
                for k in range(1, die_size + 1):
                    for key, value in state_history[-1].items():
                        if key[1] < points_to_win:
                            position = new_position(key[0], i + j + k, board_size)
                            quantum_gamestate = (position, key[1] + position)
                            if quantum_gamestate not in new_gamestates:
                                new_gamestates[quantum_gamestate] = value
                            else:
                                new_gamestates[quantum_gamestate] += value
        state_history.append(new_gamestates)
        
        score_history = []
        for states in state_history:
            scores = {}
            for k, v in states.items():
                if k[1] not in scores:
                    scores[k[1]] = v
                else:
                    scores[k[1]] += v
            score_history.append(scores)

        step_history = []
        for scores in score_history:
            steps = [0, 0]
            for k, v in scores.items():
                if k >= points_to_win:
                    steps[1] += v
                else:
                    steps[0] += v
            step_history.append(steps)

        if sum([value for key, value in new_gamestates.items() if key[1] < points_to_win]) == 0:
            break
    
    return state_history, score_history, step_history




points_to_win = 21
die_size = 3
board_size = 10

p1_states, p1_scores, p1_steps = build_player_history(6, board_size, die_size, points_to_win)
p2_states, p2_scores, p2_steps = build_player_history(7, board_size, die_size, points_to_win)

p1_total_wins = 0
p2_total_wins = 0

p1_continuations = 1
p2_continuations = 1

move = 0

while move <= max(len(p1_steps), len(p1_steps)):
    move += 1

    print(f'Move: {move}')

    print(f'P1 ply.')

    p1_continuations = p1_steps[move][0]
    p1_wins = p1_steps[move][1]
    p1_total = p1_steps[move][0] + p1_steps[move][1]
    p1_total_wins += p2_continuations * p1_wins

    print(f'P1 Continuations: {p1_continuations}')
    print(f'P1 Wins: {p1_wins}')
    print(f'P1 Total: {p1_total}')
    print(f'Cumulative P1 victories: {p1_total_wins}')

    print(f'P2 ply.')

    p2_continuations = p2_steps[move][0]
    p2_wins = p2_steps[move][1]
    p2_total =  p2_steps[move][0] + p2_steps[move][1]
    p2_total_wins += p1_continuations * p2_wins
    
    print(f'P2 Continuations: {p2_continuations}')
    print(f'P2 Wins: {p2_wins}')
    print(f'P2 Total: {p2_total}')
    print(f'Cumulative P2 victories: {p2_total_wins}')



















    

    







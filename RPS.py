import random as rand
from collections import Counter

# function to count the moves
def counter_move(move):
    if move == 'R':
        return 'P'
    elif move == 'P':
        return 'S'
    else:
        return 'R'

# check the pattern in the last three moves
def find_pattern(history):
    if len(history) < 3:
        return None
    
    last_three_moves = history[-3:]
    if last_three_moves[0] == last_three_moves[1] == last_three_moves[2]:
        return last_three_moves[0]
    else:
        return None
    
# find the move that appears not the most 
def find_not_most_common(moves):
    move_counts = Counter(moves)
    min_common_move = min(move_counts, key=move_counts.get)
    return min_common_move

# main player function
def player(prev_play, opponent_history=[], sequences={}):

    # track of opponent history
    if prev_play != '':
        opponent_history.append(prev_play)

    # # 1) BELLOW 20% chances to win
    # guess = "R"
    # if len(opponent_history) > 2:
    #     guess = opponent_history[-2]

    # return guess


    # 2) new strategy for 50% - 100% changes to win
    # if prev_play == "":
    #     # make the first move randomly
    #     return rand.choice(['R', 'S', 'P'])
    
    # # counter the opponent's last move
    # if prev_play == 'R':
    #     return 'P'
    # elif prev_play == 'P':
    #     return 'S'
    # else:
    #     return 'R'

    # 3) a second new strategy for 40% - 80% chances to win
    # if prev_play == "":
    #     return rand.choice(['R', 'P', 'S']) # first match chooses randomly
    
    # # analyzing opponent's historical moves (last and second last)
    # opponent_last_move = opponent_history[-1]
    # opponent_second_last_move = opponent_history[-2]

    # # counter the opponent's pattern
    # if opponent_last_move == opponent_second_last_move:
    #     return counter_move(opponent_last_move)
    # else:
    #     # without pattern, play randomly
    #     return rand.choice(['R', 'P', 'S'])

    # 4) a third new strategy between 43% - 80% chances to win
    # if prev_play == "":
    #     # first move in the match, play randomly
    #     return rand.choice(['R', 'P', 'S'])
    
    # # analyze opponent's pattern
    # opponent_pattern = find_pattern(opponent_history)

    # # counter the moves
    # if opponent_pattern:
    #     return counter_move(opponent_pattern)
    # else:
    #     return rand.choice(['R', 'P', 'S'])
    
    # 5) a fourth new strategy between 30% - 60% winning chances
    # if prev_play == "":
    #     # first move in the match, play randomly
    #     return rand.choice(['R', 'P', 'S'])

    # # analyze opponent's last six moves
    # last_six_moves = opponent_history[-6:]

    # # choose the move that appears not the most
    # not_most_common_move = find_not_most_common(last_six_moves)

    # return counter_move(not_most_common_move)

    # 6) best strategy to get 60% the move associated with the sequence that has the highest count
    moves = 3 # steps

    # not enough data to predict
    if len(opponent_history) <= moves:
        return rand.choice(['R', 'P', 'S'])
    
    # removes the oldest move in the history, keeping only the most recent moves
    if len(opponent_history) > moves + 1:
        opponent_history.pop(0) # index 0
    
    # increment last sequence of 4
    seq = "".join(opponent_history) # concatenates all the moves from the list
    sequences[seq] = sequences.get(seq, 0) + 1 # increments the count of the sequence, and if it is not in the dicitionary, it assigned the 1 to it

    # predict next move based on previous sequences
    seq = "".join(opponent_history[-moves:]) # the most recent moves of the opponent
    predict = max([seq+"R", seq+"P", seq+"S"],
                    key=lambda key: sequences.get(key,0))[-1] # choose the move associated with the sequence that has the highest count in sequences dinctionary
    
    return counter_move(predict)


    

# won oponent : 1
# draw        : 2
# won (me)    : 3

def won_game(action, response):
    response_map = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    response = response_map[response]

    if action == 'A' and response == 'C':
        return 1
    if action == 'B' and response == 'A':
        return 1
    if action == 'C' and response == 'B':
        return 1
    if action == response:
        return 2
    return 3

def day2_task1():
    with open("day2_task1_input.txt", "r") as f:
        move_score = {'X': 1, 'Y': 2, 'Z': 3}
        match_score = {1: 0, 2: 3, 3: 6}

        total_scores = 0
        for line in f.readlines():
            action, response = line.strip().split(' ')
            total_scores += move_score[response] + match_score[won_game(action, response)]

        print(total_scores)

# A kills C
# B kills A
# C kills B
def move_needed(action, response):
    if action == 'A' and response == 'X':
        return 'C'
    elif action == 'A' and response == 'Y':
        return 'A'
    elif action == 'A' and response == 'Z':
        return 'B'
    elif action == 'B' and response == 'X':
        return 'A'
    elif action == 'B' and response == 'Y':
        return 'B'
    elif action == 'B' and response == 'Z':
        return 'C'
    elif action == 'C' and response == 'X':
        return 'B'
    elif action == 'C' and response == 'Y':
        return 'C'
    elif action == 'C' and response == 'Z':
        return 'A'

def day2_task2():
    with open("day2_task1_input.txt", "r") as f:
        move_score = {'X': 0, 'Y': 3, 'Z': 6}
        match_score = {'A': 1, 'B': 2, 'C': 3}

        total_scores = 0
        for line in f.readlines():
            action, response = line.strip().split(' ')
            total_scores += move_score[response] + match_score[move_needed(action, response)]

        print(total_scores)

if __name__ == '__main__':
    # day2_task1()
    day2_task2()
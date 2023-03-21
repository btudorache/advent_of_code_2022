import math

def add_2d_tuples(first_tuple, second_tuple):
    return tuple(map(lambda i, j: i + j, first_tuple, second_tuple))

def is_tail_near(head_pos, tail_pos):
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos

    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        return False

    return True

def get_distance(head_pos, tail_pos):
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos

    return math.sqrt(abs(head_x - tail_x) ** 2 + abs(head_y - tail_y) ** 2)

def generate_moves(pos):
    x, y = pos
    moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)]
    return moves


def get_tail_move(head_pos, tail_pos):
    possible_moves = generate_moves(tail_pos)
    chosen_move = possible_moves[0]
    for possible_move in possible_moves[1:]:
        if get_distance(head_pos, possible_move) < get_distance(head_pos, chosen_move):
            chosen_move = possible_move

    return chosen_move


def day9_task(rope_length):
    with open("input.txt", "r") as f:
        positions = [(0, 0) for _ in range(rope_length)]
        moving_direction = (0, 0)
        visited = set()
        visited.add((0, 0))
        for line in f.readlines():
            direction, str_count = line.strip().split(" ")
            if direction == 'R':
                moving_direction = (0, 1)
            elif direction == 'U':
                moving_direction = (1, 0)
            elif direction == 'L':
                moving_direction = (0, -1)
            elif direction == 'D':
                moving_direction = (-1, 0)

            for _ in range(int(str_count)):
                positions[0] = add_2d_tuples(positions[0], moving_direction)
                for i in range(1, rope_length):
                    if not is_tail_near(positions[i - 1], positions[i]):
                        positions[i] = get_tail_move(positions[i - 1], positions[i])

                visited.add(positions[rope_length - 1])

        print(len(visited))


if __name__ == '__main__':
    day9_task(2)
    day9_task(10)
def add_2d_tuples(first_tuple, second_tuple):
    return tuple(map(lambda i, j: i + j, first_tuple, second_tuple))

def is_tail_near(head_pos, tail_pos):
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos

    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        return False

    return True

# TODO: stop using head_direction, just head_pos and tail_pos to get movement
def get_tail_move(head_pos, tail_pos, head_direction):
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos
    same_direction = head_x == tail_x or head_y == tail_y

    if same_direction:
        return add_2d_tuples(tail_pos, head_direction)
    else:
        additional_direction = (0, 0)
        tail_x, tail_y = add_2d_tuples(tail_pos, head_direction)
        if head_direction[0] != 0:
            if (abs(head_y - (tail_y + 1)) < abs(head_y + (tail_y + 1))):
                additional_direction = (0, 1)
            else:
                additional_direction = (0, -1)
        else:
            if (abs(head_x - (tail_x + 1)) < abs(head_x - (tail_x + 1))):
                additional_direction = (1, 0)
            else:
                additional_direction = (-1, 0)

        tail_pos = (tail_x, tail_y)
        return add_2d_tuples(tail_pos, additional_direction)

def print_rope_grid(positions, size):
    grid = [["." for _ in range(size)] for _ in range(size)]

    head_x, head_y = positions[0]
    if ((size - 1) - head_x >= 0 and head_y >= 0 and (size - 1) - head_x < size and head_y < size):
        grid[(size - 1) - head_x][head_y] = "H"
    for count, val in enumerate(positions[1:]):
        x, y = val
        if ((size - 1) - x >= 0 and y >= 0 and (size - 1) - x < size and y < size):
            grid[(size - 1) - x][y] = str(count + 1)
    
    for line in grid:
        print(''.join(line), end="\n")
    print(end="\n")

def day9_task1():
    with open("input.txt", "r") as f:
        head_pos = (0, 0)
        tail_pos = (0, 0)
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
                head_pos = add_2d_tuples(head_pos, moving_direction)
                if not is_tail_near(head_pos, tail_pos):
                    tail_pos = get_tail_move(head_pos, tail_pos, moving_direction)
                    visited.add(tail_pos)

        print(len(visited))


def day9_task2():
    with open("dummy_input.txt", "r") as f:
        positions = [(0, 0) for _ in range(10)]
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
                for i in range(1, 10):
                    if not is_tail_near(positions[i - 1], positions[i]):
                        positions[i] = get_tail_move(positions[i - 1], positions[i], moving_direction)
                
                print_rope_grid(positions, 6)
                visited.add(positions[9])

        print(len(visited))


if __name__ == '__main__':
    # day9_task1()
    day9_task2()
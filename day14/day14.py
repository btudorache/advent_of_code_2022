def day14_task1():
    structures = []
    max_x, max_y = -1, -1
    with open("input.txt", "r") as f:
        for line in f.readlines():
            structure = []
            stripped = line.strip()
            coords = stripped.split(" -> ")
            for coord in coords:
                y, x = coord.split(",")
                x_int, y_int = int(x), int(y)
                if x_int > max_x:
                    max_x = x_int
                if y_int > max_y:
                    max_y = y_int

                structure.append([x_int, y_int])

            structures.append(structure)

    for structure in structures:
        for pair in structure:
            pair[1] = pair[1]

    map = [['.' for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    sand_x, sand_y = 0, 500

    for structure in structures:
        for i in range(1, len(structure)):
            pair1, pair2 = structure[i - 1], structure[i]
            x1, y1 = pair1
            x2, y2 = pair2
            if x1 == x2:
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    map[x1][j] = '#'
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    map[i][y1] = '#'
            
    def out_of_bounds(x, y):
        if x >= 0 and x <= max_x and y >= 0 and y <= max_y:
            return False
        
        return True

    num_sand = 0
    keep_dropping_sand = True
    while keep_dropping_sand:
        curr_x, curr_y = sand_x, sand_y
        while True:
            if curr_x + 1 <= max_x and map[curr_x + 1][curr_y] != '#':
                curr_x += 1
            elif curr_x + 1 <= max_x and curr_y - 1 >= 0 and map[curr_x + 1][curr_y - 1] != '#':
                curr_x += 1
                curr_y -= 1
            elif curr_x + 1 <= max_x and curr_y + 1 <= max_y and map[curr_x + 1][curr_y + 1] != '#':
                curr_x += 1
                curr_y += 1
            elif out_of_bounds(curr_x + 1, curr_y) or out_of_bounds(curr_x + 1, curr_y - 1) or out_of_bounds(curr_x + 1, curr_y + 1):
                keep_dropping_sand = False
                break
            elif not out_of_bounds(curr_x, curr_y) and map[curr_x][curr_y] != '#':
                map[curr_x][curr_y] = '#'
                num_sand += 1
                break

    print(num_sand)

def print_map(map):
    for line in map:
        print(line)

def day14_task2():
    structures = []
    max_x, max_y = -1, -1
    with open("input.txt", "r") as f:
        for line in f.readlines():
            structure = []
            stripped = line.strip()
            coords = stripped.split(" -> ")
            for coord in coords:
                y, x = coord.split(",")
                x_int, y_int = int(x), int(y)
                if x_int > max_x:
                    max_x = x_int
                if y_int > max_y:
                    max_y = y_int

                structure.append([x_int, y_int])

            structures.append(structure)

    for structure in structures:
        for pair in structure:
            pair[1] = pair[1]

    # add 2 more layers to the bottom
    max_x += 2

    # add 200 more layers to the right
    max_y += 200

    map = [['.' for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    sand_x, sand_y = 0, 500

    for structure in structures:
        for i in range(1, len(structure)):
            pair1, pair2 = structure[i - 1], structure[i]
            x1, y1 = pair1
            x2, y2 = pair2
            if x1 == x2:
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    map[x1][j] = '#'
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    map[i][y1] = '#'

    for j in range(max_y + 1):
        map[max_x][j] = '#'
            
    def out_of_bounds(x, y):
        if x >= 0 and x <= max_x and y >= 0 and y <= max_y:
            return False
        
        return True

    num_sand = 0
    keep_dropping_sand = True
    while keep_dropping_sand:
        curr_x, curr_y = sand_x, sand_y
        while True:
            if curr_x + 1 <= max_x and map[curr_x + 1][curr_y] != '#':
                curr_x += 1
            elif curr_x + 1 <= max_x and curr_y - 1 >= 0 and map[curr_x + 1][curr_y - 1] != '#':
                curr_x += 1
                curr_y -= 1
            elif curr_x + 1 <= max_x and curr_y + 1 <= max_y and map[curr_x + 1][curr_y + 1] != '#':
                curr_x += 1
                curr_y += 1
            elif curr_x == sand_x and curr_y == sand_y:
                num_sand += 1
                keep_dropping_sand = False
                break
            elif map[curr_x][curr_y] != '#':
                map[curr_x][curr_y] = '#'
                num_sand += 1
                break

    print(num_sand)


if __name__ == '__main__':
    day14_task1()
    day14_task2()
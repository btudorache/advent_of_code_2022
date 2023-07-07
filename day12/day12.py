import string

def solve(is_task2 = False):
    char_map = {char: i for i, char in enumerate(string.ascii_lowercase)}

    with open("input.txt", "r") as f:
        lines = f.readlines()
        start = None
        end = None
        parsed_lines = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i, line in enumerate(lines):
            stripped = line.strip()
            parsed_line = []
            for j, char in enumerate(stripped):
                if char == 'S':
                    parsed_line.append(0)
                    start = (i, j)
                elif char == 'E':
                    parsed_line.append(25)
                    end = (i, j)
                else:
                    parsed_line.append(char_map[char])
            parsed_lines.append(parsed_line)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = [end]
        visited = [[-1 for _ in range(len(parsed_lines[0]))] for _ in range(len(parsed_lines))]
        visited[end[0]][end[1]] = 0
        while len(queue) > 0:
            node_x, node_y = queue.pop(0)
            for dir_x, dir_y in directions:
                new_x = node_x + dir_x
                new_y = node_y + dir_y
                if new_x < 0 or new_x >= len(parsed_lines) or new_y < 0 or new_y >= len(parsed_lines[0]):
                    continue

                if visited[new_x][new_y] == -1 and parsed_lines[node_x][node_y] - parsed_lines[new_x][new_y] <= 1:
                    visited[new_x][new_y] = visited[node_x][node_y] + 1
                    queue.append((new_x, new_y))

        if not is_task2:
            print(visited[start[0]][start[1]])
        else:   
            min_path = 99999
            for i in range(len(parsed_lines)):
                for j in range(len(parsed_lines[0])):
                    if parsed_lines[i][j] == 0 and visited[i][j] != -1:
                        min_path = min(min_path, visited[i][j])
            print(min_path)

def day12_task1():
    solve()

def day12_task2():
    solve(True)


if __name__ == '__main__':
    day12_task1()
    day12_task2()
# OPTIMIZATION DIRECTION:
# 2 DP ARRAYS (ONE ON ROWS, ONE ON LINES)
def day8_task1():
    with open("input.txt", "r") as f:
        trees = []
        visited_cache = []
        for line in f.readlines():
            tree_line = []
            visited_cache_line = []
            for tree in line.strip():
                tree_line.append(int(tree))
                visited_cache_line.append([0, 0, 0, 0])
            trees.append(tree_line)
            visited_cache.append(visited_cache_line)

        rows = len(trees)
        cols = len(trees[0])

        clear_trees = rows * 2 + cols * 2 - 4
        # DIRECTIONS
        # 0 - coming from up
        # 1 - coming from down
        # 2 - coming from left
        # 3 - coming from right
        def find_clear_trees(row, col, direction):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return -1

            nonlocal trees
            nonlocal clear_trees
            nonlocal visited_cache
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                visited_cache[row][col] = [trees[row][col] for _ in range(4)]
                return trees[row][col]

            if visited_cache[row][col][direction] != 0:
                return visited_cache[row][col][direction]

            if direction == 0:
                up = find_clear_trees(row + 1, col, 0)
                visited_cache[row][col][direction] = max(trees[row][col], up)
            elif direction == 1:
                down = find_clear_trees(row - 1, col, 1)
                visited_cache[row][col][direction] = max(trees[row][col], down)
            elif direction == 2:
                left = find_clear_trees(row, col - 1, 2)
                visited_cache[row][col][direction] = max(trees[row][col], left)
            elif direction == 3:
                right = find_clear_trees(row, col + 1, 3)
                visited_cache[row][col][direction] = max(trees[row][col], right)

            return visited_cache[row][col][direction]

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                up = find_clear_trees(i + 1, j, 0)
                down = find_clear_trees(i - 1, j, 1)
                left = find_clear_trees(i, j - 1, 2)
                right = find_clear_trees(i, j + 1, 3)

                if trees[i][j] > min(up, down, left, right):
                    clear_trees += 1

                visited_cache[i][j][0] = max(trees[i][j], up)
                visited_cache[i][j][1] = max(trees[i][j], down)
                visited_cache[i][j][2] = max(trees[i][j], left)
                visited_cache[i][j][3] = max(trees[i][j], right)
                
        print(clear_trees)

            
def day8_task2():
    with open("input.txt", "r") as f:
        trees = []
        for line in f.readlines():
            tree_line = []
            for tree in line.strip():
                tree_line.append(int(tree))
            trees.append(tree_line)

        rows = len(trees)
        cols = len(trees[0])

        highset_view_distance = 0
        def find_view_distance(row, col, direction, tree_val):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            nonlocal trees
            if trees[row][col] >= tree_val:
                return 1

            if direction == 0:
                return 1 + find_view_distance(row + 1, col, direction, tree_val)
            elif direction == 1:
                return 1 + find_view_distance(row - 1, col, direction, tree_val)
            elif direction == 2:
                return 1 + find_view_distance(row, col - 1, direction, tree_val)
            elif direction == 3:
                return 1 + find_view_distance(row, col + 1, direction, tree_val)

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                up = find_view_distance(i + 1, j, 0, trees[i][j])
                down = find_view_distance(i - 1, j, 1, trees[i][j])
                left = find_view_distance(i, j - 1, 2, trees[i][j])
                right = find_view_distance(i, j + 1, 3, trees[i][j])

                area = up * down * left * right
                if area > highset_view_distance:
                    highset_view_distance = area

        print(highset_view_distance)

if __name__ == '__main__':
    # day8_task1()
    day8_task2()
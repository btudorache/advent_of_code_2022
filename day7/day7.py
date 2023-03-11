class Directory:
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = {}

def get_initial_directory():
    initial = Directory(None, "/")
    return initial

def calculate_sums(root):
    if root.size != 0:
        return root.size

    for value in root.children.values():
        if type(value) is int:
            root.size += value
        else:
            root.size += calculate_sums(value)

    return root.size


def day7_task1_2():
    with open("input.txt", "r") as f:
        root = get_initial_directory()
        current = root
        total_sum = 0
        for line in f.readlines()[1:]:
            stripped = line.strip()
            if stripped == "$ cd ..":
                for value in current.children.values():
                    if type(value) is int:
                        current.size += value
                    else:
                        current.size += value.size

                if current.size <= 100000:
                    total_sum += current.size
                current = current.parent
            elif stripped.startswith("$ cd"):
                changed_to = stripped.split(' ')[2]
                current = current.children[changed_to]
            elif stripped == "$ ls":
                continue
            elif stripped.startswith("dir"):
                _, dir_name = stripped.split(' ')
                current.children[dir_name] = Directory(current, dir_name)
            else:
                size, file_name = stripped.split(' ')
                parsed_size = int(size)
                current.children[file_name] = parsed_size

        print(f"Task 1 total sum: {total_sum}")

        calculate_sums(root)

        free_space = 70000000 - root.size
        needed_space = 30000000 - free_space

        found_directory_size = 999999999
        def find_directory_size(root):
            nonlocal found_directory_size
            for value in root.children.values():
                if type(value) is not int:
                    find_directory_size(value)
                    if value.size < found_directory_size and value.size > needed_space:
                        found_directory_size = value.size
        find_directory_size(root)

        print(f"Task 2 needed size: {found_directory_size}")

if __name__ == '__main__':
    day7_task1_2()
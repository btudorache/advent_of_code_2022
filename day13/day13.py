def parse_list(list_string, start):
    parsed_list = []
    i = start + 1
    while i < len(list_string):
        if list_string[i].isdigit():
            digit_start = i
            while list_string[i].isdigit():
                i += 1
            parsed_list.append(int(list_string[digit_start:i]))
            continue
        elif list_string[i] == '[':
            inner_parsed_list, end_index = parse_list(list_string, i)
            parsed_list.append(inner_parsed_list)
            i = end_index + 1
            continue
        elif list_string[i] == ']':
            return parsed_list, i
        elif list_string[i] == ',':
            i += 1

    return parsed_list, None

def verify_mixed_lists(left, right):
    i = 0
    while i < len(left) and i < len(right):
        if isinstance(left[i], int) and isinstance(right[i], list):
            return verify_mixed_lists([left[i]], right[i])
        elif isinstance(right[i], int) and isinstance(left[i], list):
            return verify_mixed_lists(left[i], [right[i]])
        elif left[i] < right[i]:
            return True
        elif left[i] > right[i]:
            return False
        i += 1

    return True

def verify_lists(left, right):
    i = 0
    while True:
        if i >= len(left) and i < len(right):
            return True
        elif i >= len(right) and i < len(left):
            return False
        elif i >= len(right) and i >= len(left):
            return True
        elif isinstance(left[i], int) and isinstance(right[i], int) and left[i] > right[i]:
            return False
        elif isinstance(left[i], list) and isinstance(right[i], list):
            is_correct_order = verify_lists(left[i], right[i])
            if not is_correct_order:
                return False
        elif isinstance(left[i], list) or isinstance(right[i], list):
            is_correct_order = None
            if isinstance(left[i], int):
                is_correct_order = verify_mixed_lists([left[i]], right[i])
            elif isinstance(right[i], int):
                is_correct_order = verify_mixed_lists(left[i], [right[i]])

            if is_correct_order != None and not is_correct_order:
                return False

        i += 1

def day13_task1():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        index_sum = 0
        for i in range(0, len(lines), 3):
            left_stripped = lines[i].strip()
            left = parse_list(left_stripped, 0)[0]
            right_stripped = lines[i+1].strip()
            right = parse_list(right_stripped, 0)[0]

            is_correct_order = verify_lists(left, right)
            if is_correct_order:
                index_sum += ((i // 3) + 1)

        print(index_sum)

def day13_task2():
    pass


if __name__ == '__main__':
    day13_task1()
    day13_task2()
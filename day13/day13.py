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


def verify_lists(left, right):
    check_len = min(len(left), len(right))
    for i in range(check_len):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] > right[i]:
                return False
            elif left[i] < right[i]:
                return True
        else:
            left_elem = [left[i]] if isinstance(left[i], int) else left[i]
            right_elem = [right[i]] if isinstance(right[i], int) else right[i]
            lists_valid = verify_lists(left_elem, right_elem)
            if lists_valid != None:
                return lists_valid

    if len(right) < len(left):
        return False
    elif len(right) > len(left):
        return True

    return None


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
    lower_divider, higher_divider = [[2]], [[6]]
    lower, between = 0, 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            stripped = line.strip()
            if stripped != '':
                parsed = parse_list(stripped, 0)[0]
                if verify_lists(parsed, lower_divider):
                    lower += 1
                elif verify_lists(parsed, higher_divider):
                    between += 1
        
        print((lower + 1) * (lower + between + 2))


if __name__ == '__main__':
    day13_task1()
    day13_task2()
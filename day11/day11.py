import math

class Monkey:
    def __init__(self, items, operation, operation_params, test_function, test_number, true_test_monkey, false_test_monkey):
        self.items = items
        self.operation = operation
        self.operation_params = operation_params
        self.test_function = test_function
        self.test_number = test_number
        self.true_test_monkey = true_test_monkey
        self.false_test_monkey = false_test_monkey
        self.inspected_items = 0

MONKEY_DATA_LINES = 6

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def solve(num_rounds, task2 = False):
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = list(filter(lambda line: line.strip() != '', lines))
        operation_params = []
        monkey_list = []
        super_test_number = 1
        for i in range(len(lines) // MONKEY_DATA_LINES):
            starting_items_line = lines[i * MONKEY_DATA_LINES + 1].strip()
            starting_items = list(map(lambda str_item: int(str_item), starting_items_line[15:].split(", ")))

            operation_params = lines[i * MONKEY_DATA_LINES + 2].strip()[17:].split(" ")
            operation_fnc = (lambda x, operation_params : (int(operation_params[0]) if operation_params[0].isnumeric() else x) * (int(operation_params[2]) if operation_params[2].isnumeric() else x)) \
                                if operation_params[1] == '*' else \
                            (lambda x, operation_params : (int(operation_params[0]) if operation_params[0].isnumeric() else x) + (int(operation_params[2]) if operation_params[2].isnumeric() else x))
            test_number = int(lines[i * MONKEY_DATA_LINES + 3].strip()[19:])
            super_test_number = lcm(super_test_number, test_number)
            test_fnc = lambda x, test_number : x % test_number == 0

            true_test_monkey = int(lines[i * MONKEY_DATA_LINES + 4].strip()[25:])
            false_test_monkey = int(lines[i * MONKEY_DATA_LINES + 5].strip()[25:])

            monkey_list.append(Monkey(starting_items, operation_fnc, operation_params, test_fnc, test_number, true_test_monkey, false_test_monkey))

        for _ in range(num_rounds):
            for monkey in monkey_list:
                monkey.inspected_items += len(monkey.items)
                for item_worry in monkey.items:
                    final_worry = monkey.operation(item_worry, monkey.operation_params) % super_test_number if task2 else monkey.operation(item_worry, monkey.operation_params) // 3
                    if (monkey.test_function(final_worry, monkey.test_number)):
                        monkey_list[monkey.true_test_monkey].items.append(final_worry)
                    else:
                        monkey_list[monkey.false_test_monkey].items.append(final_worry)
                monkey.items = []

        monkey_list = sorted(monkey_list, key=lambda monkey: monkey.inspected_items, reverse=True)
        print(monkey_list[0].inspected_items * monkey_list[1].inspected_items)

def day11_task1():
    solve(20)

def day11_task2():
    solve(10000, True)


if __name__ == '__main__':
    day11_task1()
    day11_task2()
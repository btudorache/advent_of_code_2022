# Machine states:
# 0 - idle
# 1 - add phase 1
def day10_task1():
    with open("input.txt", "r") as f:
        total_strength = 0
        cicle = 1
        x = 1
        state = 0
        lines = f.readlines()
        curr_line = 0
        curr_args = []
        while curr_line < len(lines):
            if state == 0:
                command = lines[curr_line]
                curr_line += 1
                if command.startswith("addx"):
                    state = 1
                    _, arg = command.strip().split(" ")
                    curr_args.append(int(arg))
            elif state == 1:
                state = 0
                x += curr_args[0]
                curr_args.clear()
            cicle += 1

            if (cicle - 20) % 40 == 0:
                total_strength += cicle * x
                # print(f'cicle: {cicle} with reg x: {x} and power: {cicle * x}')

        print(total_strength)


# Machine states:
# 0 - idle
# 1 - add phase 1
def day10_task2():
    with open("input.txt", "r") as f:
        drawing = []
        drawing_row = []

        cicle = 1
        x = 1
        state = 0
        lines = f.readlines()
        curr_line = 0
        curr_args = []
        while curr_line < len(lines):
            if state == 0:
                command = lines[curr_line]
                curr_line += 1
                if command.startswith("addx"):
                    state = 1
                    _, arg = command.strip().split(" ")
                    curr_args.append(int(arg))
            elif state == 1:
                state = 0
                x += curr_args[0]
                curr_args.clear()

            crt_pos = cicle % 40
            if crt_pos == x - 1 or crt_pos == x or crt_pos == x + 1:
                drawing_row.append("#")
            else:
                drawing_row.append(".")

            if crt_pos == 39:
                drawing.append([x for x in drawing_row])
                drawing_row.clear()

            cicle += 1

        complete_drawing = []
        for row in drawing:
            complete_drawing.append("".join(row))
        print("\n".join(complete_drawing))


if __name__ == '__main__':
    day10_task1()
    day10_task2()

def day1_task1():
    with open("day1_task1_input.txt", "r") as f:
        curr_sum = 0
        max_sum = 0
        for line in f.readlines():
            if line.strip() == '':
                max_sum = curr_sum if curr_sum > max_sum else max_sum
                curr_sum = 0
            else:
                curr_sum += int(line)
        print(max_sum)

def day1_task2():
    with open("day1_task1_input.txt", "r") as f:
        sums = []
        curr_sum = 0
        for line in f.readlines():
            if line.strip() == '':
                sums.append(curr_sum)
                curr_sum = 0
            else:
                curr_sum += int(line)
        print(sum(sorted(sums, reverse=True)[:3]))


if __name__ == '__main__':
    day1_task1()
    day1_task2()
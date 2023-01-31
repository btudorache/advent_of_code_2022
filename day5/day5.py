def day5_task1():
    with open("input.txt", "r") as f:
        lists = [[], ['Z', 'J', 'N', 'W', 'P', 'S'], ['G', 'S', 'T'], ['V', 'Q', 'R', 'L', 'H'], ['V', 'S', 'T', 'D'], ['Q', 'Z', 'T', 'D', 'B', 'M', 'J'], ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L'], ['L', 'P', 'M', 'W', 'G', 'T', 'J'], ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H'], ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']]
        for line in f.readlines()[10:]:
            words = line.strip().split(' ')
            num = int(words[1])
            src = int(words[3])
            dst = int(words[5])
            for _ in range(num):
                lists[dst].append(lists[src].pop())

        top = []
        for st in lists[1:]:
            top.append(st[-1])

        print(''.join(top))


def day5_task2():
    with open("input.txt", "r") as f:
        lists = [[], ['Z', 'J', 'N', 'W', 'P', 'S'], ['G', 'S', 'T'], ['V', 'Q', 'R', 'L', 'H'], ['V', 'S', 'T', 'D'], ['Q', 'Z', 'T', 'D', 'B', 'M', 'J'], ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L'], ['L', 'P', 'M', 'W', 'G', 'T', 'J'], ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H'], ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']]
        for line in f.readlines()[10:]:
            words = line.strip().split(' ')
            num = int(words[1])
            src = int(words[3])
            dst = int(words[5])
            curr_elems = []
            for _ in range(num):
                curr_elems.append(lists[src].pop())
            curr_elems.reverse()
            lists[dst] += curr_elems

        top = []
        for st in lists[1:]:
            top.append(st[-1])

        print(''.join(top))



if __name__ == '__main__':
    day5_task1()
    day5_task2()
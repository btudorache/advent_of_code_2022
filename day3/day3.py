from collections import Counter
import string

def day3_task1():
    with open("task1_input.txt", "r") as f:
        priority = 0
        for line in f.readlines():
            chosen = ''
            stripped = line.strip()

            cnt1 = Counter()
            for letter in line[:(len(stripped) // 2)]:
                cnt1[letter] += 1

            cnt2 = Counter()
            for letter in line[(len(stripped) // 2):]:
                cnt2[letter] += 1
                if cnt2[letter] >= 1 and cnt1[letter] >= 1:
                    chosen = letter

            curr_prio = string.ascii_letters.find(chosen) + 1
            print(curr_prio, chosen)
            priority += curr_prio


        print(priority)

    
def day3_task2():
    with open("task1_input.txt", "r") as f:
        priority = 0
        lines = f.readlines()

        for i in range(len(lines) // 3):
            chosen = ''

            first_line = lines[i * 3].strip()
            cnt1 = Counter(first_line)
           
            second_line = lines[i * 3 + 1].strip()
            cnt2 = Counter(second_line)

            third_line = lines[i * 3 + 2].strip()
            cnt3 = Counter()
            for letter in third_line:
                cnt3[letter] += 1
                if cnt1[letter] >= 1 and cnt2[letter] >= 1:
                    chosen = letter

            curr_prio = string.ascii_letters.find(chosen) + 1
            priority += curr_prio

        print(priority)



if __name__ == '__main__':
    day3_task1()
    day3_task2()
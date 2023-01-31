def day4_task1():
    with open("task1_input.txt", "r") as f:
        pairs = 0
        for line in f.readlines():
            first, second = line.split(',')

            first_start, first_end = first.split('-')
            first_start, first_end = int(first_start), int(first_end)  
            
            second_start, second_end = second.split('-')
            second_start, second_end = int(second_start), int(second_end)  

            if first_start >= second_start and first_end <= second_end:
                pairs += 1
            elif second_start >= first_start and second_end <= first_end:
                pairs += 1

        print(pairs)

def day4_task2():
    with open("task1_input.txt", "r") as f:
        pairs = 0
        for line in f.readlines():
            first, second = line.split(',')

            first_start, first_end = first.split('-')
            first_start, first_end = int(first_start), int(first_end)  
            
            second_start, second_end = second.split('-')
            second_start, second_end = int(second_start), int(second_end)  

            if (first_end >= second_start and first_start <= second_end) or (second_end >= first_start and second_start <= first_end):
                pairs += 1

        print(pairs)



if __name__ == '__main__':
    day4_task1()
    day4_task2()
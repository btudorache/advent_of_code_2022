from collections import Counter

def check_all_different(counter):
    for elem, cnt in counter.items():
        if cnt != 1:
            return False

    return True

def day6_task(seq_size):
    with open("input.txt", "r") as f:
        inp = f.readlines()[0]
        cnt = Counter()
        for i in range(seq_size - 1):
            cnt[inp[i]] += 1

        siz = seq_size - 1
        for i, letter in enumerate(inp[(seq_size - 1):]):
            # print(i, letter, cnt, inp[i])
            if cnt[letter] == 0 and check_all_different(cnt):
                print(siz + 1)
                return
            else:
                cnt[inp[i]] -= 1
                if cnt[inp[i]] == 0:
                    del cnt[inp[i]]
                cnt[letter] += 1
                siz += 1

        print('end not reached')


if __name__ == '__main__':
    day6_task(4)
    day6_task(14)
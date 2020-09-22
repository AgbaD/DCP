#!/usr/bin/python3
# Author: @AgbaD | @Agba_dr3

mapping = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g',
    8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
    15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
    22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}


def num_d(msg):
    # 1111111
    answers = []
    msg = str(msg)
    length = len(msg)
    i = 1
    while i < length:
        j = 0
        count = 0
        answer = []
        while j < length:
            k = ''
            for i in range(j, j+i):
                k += msg[i]
                print(k)
                print()
            print(int(k))
            answer.append(mapping[int(k)])
            print(answer)
            """except IndexError:
                val = count * i
                answer.append(mapping[msg[int(val)]])"""
            count += 1
            j += 1
        i += 1
        answers.append(answer)

    return len(answers)


if __name__ == "__main__":
    msg1 = 1111111
    msg2 = 323
    msg3 = 9020
    msg4 = 'sds'
    print(num_d(msg1))
    print(num_d(msg2))
    print(num_d(msg3))
    print(num_d(msg4))

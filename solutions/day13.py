#!usr/bin/python3
# Author: @AgbaD | @Agba_dr3


def distinct(s, k):
    a = len(s)
    main = []
    d = []
    count = 0
    i = 0
    while i < a:
        try:
            if s[i] == s[i-1] or s[i] in d:
                if s[i] != s[i-1]:
                    # check count
                    if count < k:
                        d.append(s[i-1])
                        count += 1
                    else:
                        main.append(d)
                        d = []
                        count = 0
                """if len(d) >= k:
                    return ''.join(d)"""
                main.append(d)
                d = []
                count = 0
            else:
                if count < k:
                    d.append(s[i-1])
                    count += 1
                else:
                    main.append(d)
                    d = []
                    count = 0
        except:
            pass
        i += 1
    length = 0
    ans = ''
    for value in main:
        if len(value) > length:
            ans = value
            length = len(value)
    return ans


if __name__ == "__main__":
    k = 2
    s = 'abcba'
    print(distinct(s, k))

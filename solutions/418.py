#!usr/bin/python
# author:   @AgbaD | @agba_dr3


def get_bonus(arr):
    ans = [None] * len(arr)
    ans[0] = 1
    bonus = 2
    for i in range(len(arr) - 1):
        if arr[i+1] > arr[i]:
            ans[i+1] = bonus
            bonus += 1
        else:
            j = 1
            # ans[i+1]
            while j < len(arr)-1:
                if arr[i-j] < arr[i+1]:
                    ans[i+1] = ans[i-j]
                    break
                j += 1
    return ans


if __name__ == "__main__":
    a = [10, 40, 200, 1000, 60, 30]
    print(get_bonus(a))

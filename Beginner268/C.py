# TLE
from collections import deque

def main():
    N = input()
    p_list = list(map(int, input().split()))
    deque_p_list = deque(p_list)
    max_val = 0
    for i in range(len(p_list)):
        deque_p_list.rotate(1)
        tmp_p_list = list(deque_p_list)
        pls_count = 0
        for ind, tp in enumerate(tmp_p_list):
            if ind == 0:
                tp_left = tmp_p_list[-1]
                tp_right = tmp_p_list[ind+1]
            elif ind == len(tmp_p_list) - 1:
                tp_left = tmp_p_list[ind-1]
                tp_right = tmp_p_list[0]
            else:
                tp_left = tmp_p_list[ind-1]
                tp_right = tmp_p_list[ind+1]

            if [tp, tp_left, tp_right].count(ind):
                pls_count += 1

        if max_val < pls_count:
            max_val = pls_count

    print(max_val)

    
if __name__ == "__main__":
    main()
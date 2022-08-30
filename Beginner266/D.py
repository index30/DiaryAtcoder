import numpy as np
import itertools


def main():
    N = int(input())
    takahashi_list = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        takahashi_list.append(tmp)
    takahashi_list = [tmp for tmp in takahashi_list if tmp[0] >= tmp[1]]
    t_len = len(takahashi_list)
    result = []
    for n in range(1, t_len+1):
        for conb in itertools.combinations(takahashi_list, n):
            result.append(list(conb))  # タプルをリスト型に変換
    # print(result)
    final = 0
    for res in result:
        out_count = 0
        A_sum = 0
        count = 0
        while count < len(res):
            t, x, A = res[count]
            if t < x:
                out_count += 1
            A_sum += A
            res = [[t2-t, x2-x, A2] for t2, x2, A2 in res]
            count += 1
        if (out_count == 0) and (final < A_sum):
            print(A_sum)
            final = A_sum

    print(final)


if __name__ == "__main__":
    main()

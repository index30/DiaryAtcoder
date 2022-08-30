import numpy as np


def main():
    H1, W1 = list(map(int, input().split()))
    A1_list = []
    for _ in range(H1):
        tmp_A1 = list(map(int, input().split()))
        A1_list.append(tmp_A1)

    H2, W2 = list(map(int, input().split()))
    A2_list = []
    for _ in range(H2):
        tmp_A2 = list(map(int, input().split()))
        A2_list.append(tmp_A2)

    new_A1_list = []
    for a1 in A1_list:
        for a2 in A2_list:
            check_r = [ta2 for ta2 in a2 if ta2 in a1]
            if len(check_r) == W2:
                new_A1_list.append(a1)

    A1_list = new_A1_list
    new_H2, new_W2 = np.array(A2_list).T.shape
    A1_list = list(np.array(A1_list).T)
    A2_list = list(np.array(A2_list).T)

    new_A1_list = []
    for a1t in A1_list:
        for a2t in A2_list:
            check_c = [ta2 for ta2 in a2t if ta2 in a1t]
            if len(check_c) == new_W2:
                new_A1_list.append(a1t)

    A1_list = new_A1_list
    A1_list = list(np.array(A1_list).T)
    A2_list = list(np.array(A2_list).T)

    out_count = 0

    for a1, a2 in zip(A1_list, A2_list):
        if list(a1) != list(a2):
            out_count += 1

    if len(A1_list) > 0 and (out_count == 0):
        print("Yes")
    else:
        A1_list = np.unique(A1_list, axis=0)
        A2_list = np.unique(A2_list, axis=0)
        if np.array(A1_list).ndim > 1:
            A1_list = np.unique(A1_list, axis=1)
        if np.array(A2_list).ndim > 1:
            A2_list = np.unique(A2_list, axis=1)
        out_count = 0

        print(A1_list)
        print(A2_list)
        for a1, a2 in zip(A1_list, A2_list):
            if list(a1) != list(a2):
                out_count += 1
        if len(A1_list) > 0 and (out_count == 0):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()

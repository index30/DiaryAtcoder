import numpy as np


def main():
    H, W = list(map(int, input().split()))
    S_list = [list(input()) for _ in range(H)]
    S_numpy = np.asarray(S_list)
    NO_flg = 0
    for h in range(1, H-1):
        for w in range(1, W-1):
            if S_numpy[h, w] == "#":
                if (S_numpy[h-1][w] == '.') and (S_numpy[h][w-1] == '.')\
                    and (S_numpy[h][w+1] == '.') \
                        and (S_numpy[h+1][w] == '.'):
                    NO_flg = 1

        if S_numpy[h, 0] == "#":
            if (S_numpy[h-1][0] == '.') and (S_numpy[h][1] == '.')\
                    and (S_numpy[h+1][0] == '.'):
                NO_flg = 1
        if S_numpy[h, W-1] == "#":
            if (S_numpy[h-1][W-1] == '.') and (S_numpy[h][W-2] == '.')\
                    and (S_numpy[h+1][W-1] == '.'):
                NO_flg = 1

    for w in range(1, W-1):
        if S_numpy[0, w] == "#":
            if (S_numpy[0][w-1] == '.')\
                    and (S_numpy[0][w+1] == '.') and (S_numpy[1][w] == '.'):
                NO_flg = 1
        if S_numpy[H-1, w] == "#":
            if (S_numpy[H-1][w-1] == '.')\
                    and (S_numpy[H-1][w+1] == '.') and (S_numpy[H-2][w] == '.'):
                NO_flg = 1

    if S_numpy[0, 0] == "#":
        if (S_numpy[0][1] == '.') and (S_numpy[1][0] == '.'):
            NO_flg = 1

    if S_numpy[H-1, W-1] == "#":
        if (S_numpy[H-2][W-1] == '.') and (S_numpy[H-1][W-2] == '.'):
            NO_flg = 1

    if NO_flg:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()

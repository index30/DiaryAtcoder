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
                        and (S_numpy[h][w+1] == '.') and (S_numpy[h+1][w] == '.'):
                    NO_flg = 1

    for h in range(H):
        if S_numpy[h, w] == "#" and h != (H-1):
            if (S_numpy[h-1][w] == '.') and (S_numpy[h][w-1] == '.')\
                    and (S_numpy[h][w+1] == '.') and (S_numpy[h+1][w] == '.'):
                NO_flg = 1
        else:
            pass

    for sn in S_numpy:
        tmp = []
        for s in sn:
            if s == "#"

    print(S_list)
    print(S_numpy[:, 0])


if __name__ == "__main__":
    main()

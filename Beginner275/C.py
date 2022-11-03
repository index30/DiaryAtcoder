import itertools
import numpy as np

def tangent_angle(u: np.ndarray, v: np.ndarray):
    i = np.inner(u, v)
    n = np.linalg.norm(u) * np.linalg.norm(v)
    c = i / n
    return c#np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

def main():
    S_list = []
    gra_num = 4
    for i in range(9):
        S = input()
        for j, s in enumerate(S):
            if s == "#":
                S_list.append((i, j))
    tmp = list(itertools.combinations(S_list, gra_num))
    count = 0
    for t in tmp:
        gravity = np.sum(t, axis=0)/gra_num
        tmp_list, rad_list = [], []

        v0 = gravity - t[0]
        tmp_list.append(v0)

        for j in range(1, gra_num):
            vec = gravity - t[j]
            tmp_list.append(vec)
            rad_list.append(tangent_angle(vec, v0))
        if (len(np.unique(tmp_list)) == 1) and (len(np.unique(rad_list)) == 2):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
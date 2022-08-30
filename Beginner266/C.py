import numpy as np


def main():
    Axy = list(map(int, input().split()))
    Bxy = list(map(int, input().split()))
    Cxy = list(map(int, input().split()))
    Dxy = list(map(int, input().split()))
    out_count = 0

    for p1, p2, p3 in [(Axy, Bxy, Cxy), (Bxy, Cxy, Dxy), (Cxy, Dxy, Axy), (Dxy, Axy, Bxy)]:
        p1 = np.array(p1)
        p2 = np.array(p2)
        p3 = np.array(p3)
        u = p1 - p2
        v = p3 - p2
        dir1 = np.rad2deg(np.arctan2(u[1], u[0]))  # v1の方向
        dir2 = np.rad2deg(np.arctan2(v[1], v[0]))  # v2の方向

        r = dir2 - dir1
        if r < 0:
            degree = abs(r)
        else:
            degree = 360 - r

        if degree > 180:
            out_count += 1

    if out_count == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

import numpy as np


def main():
    H, W = list(map(int, input().split()))
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))

    A = np.array(A)
    B = A.T

    for i in range(W):
        print(" ".join(map(str, list(B[i]))))


if __name__ == "__main__":
    main()

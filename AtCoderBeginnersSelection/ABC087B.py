def calc_way(A, B, C, X):
    if (500 * A + 100 * B + 50 * C) < X:
        return 0
    # mul500 = X // 500
    # result500 = X - 500 * mul500
    # mul100 = result500 // 100
    # result100 = result500 - 100 * mul100
    # mul50 = result100 // 50
    # result50 = result100 - 50 * mul50
    # if result50 > 0:
    #     pass


def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    result500 = X // 500
    result100 = result500 // 100
    result50 = result100 // 50


if __name__ == "__main__":
    main()

# WA。ちょうどN枚になる必要がある
def judge_eq(x, y, z, Y):
    if (10000 * x + 5000 * y + 1000 * z) == Y:
        return True
    return False


def main():
    N, Y = list(map(int, input().split()))
    count = 0
    for x in range(N+1):
        for y in range(N-x+1):
            if judge_eq(x, y, N-x-y, Y) and count == 0:
                count = 1
                print("{} {} {}".format(x, y, N-x-y))
    if count == 0:
        print("-1 -1 -1")


if __name__ == "__main__":
    main()

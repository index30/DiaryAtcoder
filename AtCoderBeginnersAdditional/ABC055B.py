# from functools import reduce
# from operator import mul


def main():
    N = int(input())
    power = 1
    for x in range(1, N+1):
        power = (power*x) % (10**9 + 7)
    print(power)

    # TLEになる
    # power = reduce(mul, [x for x in range(1, N+1)])
    # print(power % (10**9 + 7))


if __name__ == "__main__":
    main()

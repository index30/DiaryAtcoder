import math


def main():
    X, Y = list(map(int, input().split()))
    print(max(math.ceil(float((Y-X)/10)), 0))


if __name__ == "__main__":
    main()

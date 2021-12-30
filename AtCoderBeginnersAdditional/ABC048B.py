# https://atcoder.jp/contests/abc048/tasks/abc048_b

def main():
    a, b, x = list(map(int, input().split()))
    if a % x != 0:
        left = a//x + 1
    else:
        left = a//x
    print(len(range(left, b//x+1)))


if __name__ == "__main__":
    main()

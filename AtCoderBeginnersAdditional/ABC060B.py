# https://atcoder.jp/contests/abc060/tasks/abc060_b

def main():
    A, B, C = list(map(int, input().split()))
    count_flg = 0
    for i in range(1, B+1):
        if (i * A) % B == C:
            count_flg += 1

    if not count_flg:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()

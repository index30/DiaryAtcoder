# TLE
def main():
    _, Q = list(map(int, input().split()))
    A_list = list(map(int, input().split()))
    Q_list = [int(input()) for _ in range(Q)]
    for q in Q_list:
        print(sorted(A_list+[q])[::-1].index(q))


if __name__ == "__main__":
    main()

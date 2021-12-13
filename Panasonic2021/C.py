# 解説を見た上でAC確認
def main():
    N, Q = list(map(int, input().split()))
    A_list = sorted(map(int, input().split()))
    Q_list = [int(input()) for _ in range(Q)]
    for q in Q_list:
        right = N
        left = -1
        while right - left > 1:
            mid = (right + left) // 2
            if A_list[mid] >= q:
                right = mid
            else:
                left = mid
        print(N - right)


if __name__ == "__main__":
    main()

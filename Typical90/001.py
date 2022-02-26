# 二分探索問題に落とす
# 参考: https://twitter.com/e869120/status/1377027868518064129/photo/1
# K+1個以上のピースに分割した際に、長さM以上のピースに分割できているか

def main():
    N, L = list(map(int, input().split()))
    K = int(input())
    A_list = list(map(int, input().split()))

    left = -1
    right = L + 1
    while right - left > 1:
        M = left + (right - left) // 2
        cnt, pre = 0, 0
        for a in A_list:
            if (a - pre) >= M and (L - a) >= M:
                pre = a
                cnt += 1
        if cnt >= K:
            left = M
        else:
            right = M
    print(left)


if __name__ == "__main__":
    main()

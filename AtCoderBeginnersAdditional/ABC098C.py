# https://atcoder.jp/contests/abc098/tasks/arc098_a
# 回答の方向性は下記参照
# https://blog.hamayanhamayan.com/entry/2018/05/26/231744

# 累積和から算出するとAC
def main():
    N = int(input())
    S = input()
    E = [0] * N
    W = [0] * N
    min_len = 3 * (10 ** 5)
    for i in range(N):
        if S[i] == 'E':
            E[i] = 1
        else:
            W[i] = 1

    for i in range(1, N):
        E[i] += E[i - 1]
        W[i] += W[i - 1]

    for i in range(N):
        tmp_sum = 0
        if i:
            tmp_sum = W[i - 1]
        tmp_sum += E[N - 1] - E[i]
        if tmp_sum < min_len:
            min_len = tmp_sum

    print(min_len)

# 愚直にやるとTLE(2206ms)
# def main():
#     N = int(input())
#     S = input()
#     min_len = 3 * (10 ** 5)
#     for n in range(N):
#         change_list = [tmp for tmp in S[:n] if tmp == 'W'] + \
#             [tmp for tmp in S[n:] if tmp == 'E']
#         if len(change_list) < min_len:
#             min_len = len(change_list)
#     print(min_len)


if __name__ == "__main__":
    main()

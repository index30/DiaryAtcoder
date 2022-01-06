# https://atcoder.jp/contests/abc087/tasks/arc090_a

def main():
    N = int(input())
    A_list1 = list(map(int, input().split()))
    A_list2 = list(map(int, input().split()))
    candy_sums = []

    for i in range(N):
        candy_list = A_list1[1:i+1] + A_list2[i:-1]
        candy_sums.append(sum(candy_list))

    print(A_list1[0] + max(candy_sums) + A_list2[N-1])


if __name__ == "__main__":
    main()

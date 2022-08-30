import itertools


def main():
    N, K = list(map(int, input().split()))
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    A_pics = []
    for i in range(N+1):
        A_pics.extend(list(itertools.combinations(range(N), i)))

    count = 0
    for a_pics in A_pics:
        X = []
        for i in range(N):
            if i in a_pics:
                X.append(A_list[i])
            else:
                X.append(B_list[i])

        for i in range(N-1):
            if abs(X[i] - X[i+1]) <= K:
                count += 1

    if count:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

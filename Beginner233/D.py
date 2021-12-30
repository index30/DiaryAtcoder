def main():

    N, K = list(map(int, input().split()))
    A_list = list(map(int, input().split()))
    A_list = [a for a in A_list if a != 0]
    count = 0

    for r in range(N+1):
        for l in range(r):
            if sum(A_list[:l]) == sum(A_list[:r]) - K:
                count += 1

    print(count)


if __name__ == "__main__":
    main()

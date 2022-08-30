def main():
    N = int(input())
    P_list = list(map(int, input().split()))
    ind = N - 2
    count = 0
    while P_list[ind] != 1:
        ind = P_list[ind] - 2
        count += 1
    print(count+1)


if __name__ == "__main__":
    main()

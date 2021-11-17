def main():
    N = int(input())
    txy_dict = {}
    for _ in range(N):
        t, x, y = list(map(int, input().split()))
        txy_dict[t] = (x, y)

    print(txy_dict)


if __name__ == "__main__":
    main()

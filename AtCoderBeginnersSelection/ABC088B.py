def main():
    N = int(input())
    N_list = sorted(map(int, input().split()), reverse=True)
    if N > 1:
        result = sum(N_list[::2]) - sum(N_list[1::2])
        print(result)
    else:
        print(N_list[0])


if __name__ == "__main__":
    main()

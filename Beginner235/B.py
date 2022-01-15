def main():
    N = int(input())
    H_list = list(map(int, input().split()))
    pos = 0
    while pos < len(H_list)-1:
        if H_list[pos] < H_list[pos+1]:
            pos += 1
        else:
            break

    print(H_list[pos])


if __name__ == "__main__":
    main()

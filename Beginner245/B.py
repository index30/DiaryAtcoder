def main():
    _ = int(input())
    A_list = list(map(int, input().split()))
    max_A = max(A_list)
    result = max_A + 1
    for i in range(0, max_A+1):
        if i not in A_list:
            result = i
            break
    print(result)


if __name__ == "__main__":
    main()

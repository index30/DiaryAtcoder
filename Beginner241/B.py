def main():
    N, M = list(map(int, input().split()))
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    for a in A_list:
        if a in B_list:
            B_list.remove(a)
    if len(B_list) > 0:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()

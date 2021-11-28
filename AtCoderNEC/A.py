def main():
    S_list = [list(input()) for _ in range(2)]
    if S_list[0][0] == "." and S_list[1][1] == ".":
        print("No")
    elif S_list[0][1] == "." and S_list[1][0] == ".":
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()

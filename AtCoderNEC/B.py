def main():
    A, B = list(input().split())
    flg = 0
    for a, b in zip(A[::-1], B[::-1]):
        if int(a) + int(b) > 9:
            flg += 1
            break
    if flg:
        print("Hard")
    else:
        print("Easy")


if __name__ == "__main__":
    main()

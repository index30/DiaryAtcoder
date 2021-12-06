def main():
    A, B, C, D = list(map(int, input().split()))
    if (B < C) or (D < A):
        print(0)
    else:
        if (D-B) * (C-A) < 0:
            print(min(abs(D-C), abs(B-A)))
        else:
            print(min(abs(B-C), abs(D-A)))


if __name__ == "__main__":
    main()

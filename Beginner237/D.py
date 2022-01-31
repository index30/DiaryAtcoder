def main():
    N = int(input())
    S = input()
    A = [0]
    for i, s in enumerate(S):
        if s == 'L':
            A.insert(max(0, i-1), i+1)
        else:
            A.insert(i, i+1)
        print(A)

    print(A)
    print("{}".format(" ".join([a for a in A])))


if __name__ == "__main__":
    main()

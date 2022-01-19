# https://atcoder.jp/contests/abc079/tasks/abc079_c

def main():
    A, B, C, D = input()
    A, B, C, D = int(A), int(B), int(C), int(D)
    if A+B+C+D == 7:
        print("{}+{}+{}+{}=7".format(A, B, C, D))
    elif A+B+C-D == 7:
        print("{}+{}+{}-{}=7".format(A, B, C, D))
    elif A+B-C+D == 7:
        print("{}+{}-{}+{}=7".format(A, B, C, D))
    elif A-B+C+D == 7:
        print("{}-{}+{}+{}=7".format(A, B, C, D))
    elif A+B-C-D == 7:
        print("{}+{}-{}-{}=7".format(A, B, C, D))
    elif A-B+C-D == 7:
        print("{}-{}+{}-{}=7".format(A, B, C, D))
    elif A-B-C+D == 7:
        print("{}-{}-{}+{}=7".format(A, B, C, D))
    else:
        print("{}-{}-{}-{}=7".format(A, B, C, D))


if __name__ == "__main__":
    main()

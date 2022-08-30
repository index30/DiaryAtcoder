# TLE
# def f(N):
#     if N == 1:
#         seq = [(1/6)*i for i in range(1, 7)]
#         return sum(seq)
#     else:
#         seq = [(1/6)*max(i, f(N-1)) for i in range(1, 7)]
#         return sum(seq)


def main():
    N = int(input())
    result = 3.5
    if N > 1:
        for i in range(1, N):
            result2 = 0
            for j in range(1, 7):
                result2 += max(result, j)/6
            result = result2
    print(result)


if __name__ == "__main__":
    main()

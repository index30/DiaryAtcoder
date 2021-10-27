def calc_result(A, B, C, X):
    count = 0
    result = X
    a_range_num = min(int(X/500), A) + 1
    for sa in range(a_range_num):
        sa_result = result
        b_range_num = min(int(result/100), B) + 1
        for sb in range(b_range_num):
            sb_result = sa_result
            c_range_num = min(int(sb_result/50), C) + 1
            for sc in range(c_range_num):
                if sb_result - (sc * 50) == 0:
                    count += 1
            sa_result -= 100
        result -= 500
    return count


def main():
    A, B, C, X = [int(input()) for _ in range(4)]
    result = calc_result(A, B, C, X)
    print(result)


if __name__ == "__main__":
    main()

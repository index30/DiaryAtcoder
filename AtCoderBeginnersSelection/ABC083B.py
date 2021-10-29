def main():
    N, A, B = list(map(int, input().split()))
    digits = [10 ** x for x in reversed(range(1, 5))]
    results = []
    for n in range(1, N + 1):
        tmp_n = n
        vals = []
        for x in digits:
            val = tmp_n // x
            tmp_n = tmp_n - val * x
            vals.append(val)
        vals.append(tmp_n)
        sum_val = sum(vals)
        if (sum_val >= A) and (sum_val <= B):
            results.append(n)
    print(sum(results))


if __name__ == "__main__":
    main()

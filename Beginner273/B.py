def origin_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p

def main():
    X, K = list(map(int, input().split()))
    for k in range(K):
        X = origin_round(X, -(k+1))
    print(int(X))

if __name__ == "__main__":
    main()
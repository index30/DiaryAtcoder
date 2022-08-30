def main():
    target = 'atcoder'
    L, R = list(map(int, input().split()))
    print(target[L-1:R])


if __name__ == "__main__":
    main()

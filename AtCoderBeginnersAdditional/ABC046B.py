# https://atcoder.jp/contests/abc046/tasks/abc046_b

def main():
    N, K = list(map(int, input().split()))
    print(K*((K-1)**(N-1)))


if __name__ == "__main__":
    main()

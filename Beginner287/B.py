import math

def main():
    N, M = list(map(int, input().split()))
    S_list, T_list = [], []
    count = 0
    for _ in range(N):
        S = input()
        S_list.append(S[-3:])
    for _ in range(M):
        T = input()
        T_list.append(T)

    for s in S_list:
        if s in T_list:
            count += 1
    
    print(count)


if __name__ == "__main__":
    main()
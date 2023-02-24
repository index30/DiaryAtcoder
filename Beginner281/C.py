def main():
    N, T = list(map(int, input().split()))
    A_list = list(map(int, input().split()))
    target_time = T % sum(A_list)
    current_time = 0
    cumsum_time = 0
    for i, a in enumerate(A_list):
        if target_time < (a+cumsum_time):
            print(i+1, target_time - cumsum_time)
            break
        else:
            cumsum_time += a

if __name__ == "__main__":
    main()
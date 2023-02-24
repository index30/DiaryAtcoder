import math

def main():
    N = int(input())
    for_sum = 0
    against_sum = 0
    for _ in range(N):
        S = input()
        if S == 'For':
            for_sum += 1
        else:
            against_sum += 1
    
    if math.ceil(N/2) <= for_sum:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
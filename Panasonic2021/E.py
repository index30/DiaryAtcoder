# WIP

def main():
    N, X = list(map(int, input().split()))
    A_list = sorted(map(int, input().split()))
    X_ind = sum([1 if X >= a else 0 for a in A_list])
    tmp = X
    count = 0
    for a in A_list[:X_ind][::-1]:
        count += tmp // a
        tmp = tmp % a

    if X_ind < len(A_list):
        print("T<P")
        print(X)
        print(A_list[X_ind])
        tmp2 = A_list[X_ind] - X
        print(tmp2)
        print("-----")
        count2 = 0
        for a in A_list[:X_ind][::-1]:
            count2 += tmp2 // a
            tmp2 = tmp2 % a
        print(min(count, count2 + 1))
    else:
        print(count)
    print(count)


if __name__ == "__main__":
    main()

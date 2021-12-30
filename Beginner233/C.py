def main():

    N, X = list(map(int, input().split()))
    first_l_list = list(map(int, input().split()))
    l_list = [fc for fc in first_l_list[1:] if X % fc == 0]

    for n in range(N-1):
        tmp_l_list = list(map(int, input().split()))
        tmp_pred_l_list = []
        for tl in tmp_l_list[1:]:
            result = [x*tl for x in l_list if X % (x*tl) == 0]
            tmp_pred_l_list.extend(result)
        l_list = tmp_pred_l_list

    print(sum([1 for x in l_list if x == X]))


if __name__ == "__main__":
    main()

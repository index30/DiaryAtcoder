import itertools

def main():
    N, K, D = list(map(int, input().split()))
    A_list = list(map(int, input().split()))
    A_list = sorted(A_list)[::-1]
    print(A_list)
    # def _check_D(comb_list):
    #     sum_val = sum(comb_list)
    #     if sum_val%D == 0:
    #         return sum_val
    #     return -1
    # tmp = list(set(map(_check_D, list(itertools.combinations(A_list, K)))))
    # print(max(tmp))

if __name__ == "__main__":
    main()
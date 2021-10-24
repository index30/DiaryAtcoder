import numpy as np


def calc_div2(input_list, max_length):
    div_list = [1 if x % 2 == 0 else 0 for x in input_list]
    if sum(div_list) < max_length:
        return 0
    else:
        input_list = np.asarray(input_list)/2
        input_list = input_list.tolist()
        return 1 + calc_div2(input_list, max_length)


def main():
    N = int(input())
    AN_list = list(map(int, input().split()))
    result = calc_div2(AN_list, N)
    print(result)


if __name__ == "__main__":
    main()

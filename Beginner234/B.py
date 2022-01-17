import itertools
import math


def calc_len(co1, co2):
    return math.sqrt((co2[1]-co1[1])**2 + (co2[0]-co1[0])**2)


def main():
    N = int(input())
    co_list = []
    max_val = 0
    for _ in range(N):
        x, y = list(map(int, input().split()))
        co_list.append((x, y))
    for pair in itertools.combinations(co_list, 2):
        tmp = calc_len(pair[0], pair[1])
        if max_val < tmp:
            max_val = tmp
    print(max_val)


if __name__ == "__main__":
    main()

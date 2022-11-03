import collections

def main():
    N = int(input())
    A_list = list(map(int, input().split()))
    result_list = []
    for a in A_list:
        count = 0
        for a2 in list(set(A_list)):
            if a < a2:
                count += 1
        result_list.append(count)
    result_counter = collections.Counter(result_list)
    for i in range(N):
        print(result_counter.get(i, 0))


if __name__ == "__main__":
    main()

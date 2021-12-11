import collections


def main():
    N = int(input())
    S_list = [input() for _ in range(N)]
    S_counter = collections.Counter(S_list)
    print(S_counter.most_common()[0][0])


if __name__ == "__main__":
    main()

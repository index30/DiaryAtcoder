# TLE
import sys
input = sys.stdin.readline


def main():
    _, Q = list(map(int, input().split()))
    a_list = list(map(int, input().split()))

    a_dict = {}
    for a in set(a_list):
        a_dict[a] = [i for i, x in enumerate(a_list) if x == a]

    for q in range(Q):
        query = list(map(int, input().split()))
        if query[1]-1 < len(a_dict.get(query[0], [])):
            print(a_dict[query[0]][query[1]-1]+1)
        else:
            print(-1)


if __name__ == "__main__":
    main()

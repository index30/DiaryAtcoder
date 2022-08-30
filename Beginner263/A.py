import collections


def main():
    input_list = list(map(int, input().split()))
    c = collections.Counter(input_list)
    if len(c.keys()) == 2 and ((list(c.values())[0] == 2) or (list(c.values())[0] == 3)):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

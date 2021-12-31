# https://atcoder.jp/contests/abc065/tasks/abc065_b

def judge_button2(a_list, ind):
    if a_list[ind-1] == 2:
        return 1
    else:
        return 0


def main():
    N = int(input())
    a_list = [int(input()) for _ in range(N)]
    index = 1
    judge_flg = 0
    for i, _ in enumerate(range(len(a_list))):
        if judge_button2(a_list, index):
            print(i+1)
            judge_flg = 1
            break
        index = a_list[index-1]
    if not judge_flg:
        print(-1)


if __name__ == "__main__":
    main()

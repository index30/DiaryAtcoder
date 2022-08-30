import numpy


def main():
    N = int(input())
    S_list = []
    OK_count = 0
    for _ in range(N):
        S = input()
        S_list.append(S)

    row_str = ""
    for s in S_list:
        row_str += s + '/'

    column_str = ""
    for s in zip(S_list):
        column_str += "".join(s) + '/'

    tmp_list = []
    outer_white = 0
    inner_white = 0
    for rs in row_str:
        if rs != '/':
            if rs == '#':
                tmp_list.append(rs)
            elif rs == '.' and len(tmp_list) == 0 and outer_white < 2:
                outer_white += 1
            elif len(tmp_list) > 0 and inner_white < 2:
                inner_white += 1
            else:
                tmp_list = []
                outer_white = 0
                inner_white = 0
            if outer_white + inner_white > 2:
                outer_white -= 1
            over_white = outer_white + inner_white
            if len(tmp_list) > 5 or len(tmp_list) > (5 - over_white):
                OK_count += 1

    for rs in row_str[::-1]:
        if rs != '/':
            if rs == '#':
                tmp_list.append(rs)
            elif rs == '.' and len(tmp_list) == 0 and outer_white < 2:
                outer_white += 1
            elif len(tmp_list) > 0 and inner_white < 2:
                inner_white += 1
            else:
                tmp_list = []
                outer_white = 0
                inner_white = 0
            if outer_white + inner_white > 2:
                outer_white -= 1
            over_white = outer_white + inner_white
            if len(tmp_list) > 5 or len(tmp_list) > (5 - over_white):
                OK_count += 1

    for rs in column_str:
        if rs != '/':
            if rs == '#':
                tmp_list.append(rs)
            elif rs == '.' and len(tmp_list) == 0 and outer_white < 2:
                outer_white += 1
            elif len(tmp_list) > 0 and inner_white < 2:
                inner_white += 1
            else:
                tmp_list = []
                outer_white = 0
                inner_white = 0
            if outer_white + inner_white > 2:
                outer_white -= 1
            over_white = outer_white + inner_white
            if len(tmp_list) > 5 or len(tmp_list) > (5 - over_white):
                OK_count += 1

    for rs in column_str[::-1]:
        if rs != '/':
            if rs == '#':
                tmp_list.append(rs)
            elif rs == '.' and len(tmp_list) == 0 and outer_white < 2:
                outer_white += 1
            elif len(tmp_list) > 0 and inner_white < 2:
                inner_white += 1
            else:
                tmp_list = []
                outer_white = 0
                inner_white = 0
            if outer_white + inner_white > 2:
                outer_white -= 1
            over_white = outer_white + inner_white
            if len(tmp_list) > 5 or len(tmp_list) > (5 - over_white):
                OK_count += 1

    if OK_count:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

def main():
    S = input()
    S_pos = 0
    NG_flg = 0
    while len(S) > S_pos + 1:
        tmp_S = S[S_pos:S_pos+5]
        if tmp_S == "dream":
            if S[S_pos+5:S_pos+7] == "er":
                S_pos = S_pos + 7
            else:
                S_pos = S_pos + 5
        elif tmp_S == "erase":
            if S[S_pos+5:S_pos+6] == "r":
                S_pos = S_pos + 6
            else:
                S_pos = S_pos + 5
        else:
            NG_flg += 1
            break
    if NG_flg:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()

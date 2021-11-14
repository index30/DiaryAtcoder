def main():
    S = input()
    S_pos, NG_flg = 0, 0

    while len(S) > S_pos + 1:
        if S[S_pos:S_pos+11] == "dreameraser":
            S_pos = S_pos + 11
        elif S[S_pos:S_pos+10] == "dreamerase":
            S_pos = S_pos + 10
        elif S[S_pos:S_pos+7] == "dreamer":
            S_pos = S_pos + 7
        elif S[S_pos:S_pos+6] == "eraser":
            S_pos = S_pos + 6
        elif S[S_pos:S_pos+5] == "dream":
            S_pos = S_pos + 5
        elif S[S_pos:S_pos+5] == "erase":
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

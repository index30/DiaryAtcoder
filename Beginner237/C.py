def main():
    S = input()
    flg = 0
    firs, las = [], []
    for s in S:
        if s != 'a':
            break
        else:
            firs.append(s)
    for s in S[::-1]:
        if s != 'a':
            break
        else:
            las.append(s)
    tmp_len = max(0, len(las) - len(firs))
    S = "".join(['a']*tmp_len) + S

    for i, s in enumerate(S):
        if S[i] != S[len(S)-1-i]:
            flg += 1

    if not flg:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

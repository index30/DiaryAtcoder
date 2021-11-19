def main():
    N = int(input())
    ts, xs, ys = [0], [0], [0]
    flg = False
    for _ in range(N):
        t, x, y = list(map(int, input().split()))
        ts.append(t)
        xs.append(x)
        ys.append(y)

    for i in range(N):
        dt = ts[i+1] - ts[i]
        dist = abs(xs[i+1] - xs[i]) + abs(ys[i+1] - ys[i])
        if dist > dt:
            flg = False
        else:
            if (dt + dist) % 2 == 0:
                flg = True
            else:
                flg = False

    if flg == True:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

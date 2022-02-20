def main():
    x1, y1, x2, y2 = list(map(int, input().split()))
    tmp_list = [(1, 2), (2, 1), (-2, -1), (-1, -2),
                (1, -2), (-1, 2), (2, -1), (-2, 1)]
    count = 0
    for (tl_x, tl_y) in tmp_list:
        tmp_x, tmp_y = x1 + tl_x, y1 + tl_y
        if (x2 - tmp_x)**2 + (y2 - tmp_y)**2 == 5:
            count += 1
    if count:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

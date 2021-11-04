# WA。ちょうどN枚になる必要がある

def main():
    N, Y = list(map(int, input().split()))
    count_N = N
    x_count, y_count, z_count = 0, 0, 0
    rest_Y = Y
    while count_N >= 0:
        if rest_Y >= 10000:
            rest_Y = rest_Y - 10000
            x_count += 1
        elif (rest_Y < 10000) and (rest_Y >= 5000):
            rest_Y = rest_Y - 5000
            y_count += 1
        elif (rest_Y < 5000) and (rest_Y >= 1000):
            rest_Y = rest_Y - 1000
            z_count += 1
        elif (rest_Y < 1000) and (rest_Y > 0):
            print("-1 -1 -1")
        else:
            print("{} {} {}".format(x_count, y_count, z_count))
            break
        count_N -= 1
    if rest_Y > 0:
        print("-1 -1 -1")
    if (x_count + y_count + z_count) > N:
        print("-1 -1 -1")


if __name__ == "__main__":
    main()

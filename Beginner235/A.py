def main():
    str = input()
    a, b, c = int(str[0]), int(str[1]), int(str[2])
    print((100*a + 10*b + c) + (100*b + 10*c + a) + (100*c + 10*a + b))


if __name__ == "__main__":
    main()

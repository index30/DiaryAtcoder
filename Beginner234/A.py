def func_f(t):
    return t**2 + 2 * t + 3


def main():
    t = int(input())
    print(func_f(func_f(func_f(t)+t) + func_f(func_f(t))))


if __name__ == "__main__":
    main()

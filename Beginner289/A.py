def main():
    S = input()
    result = ""
    for s in S:
        if s == '0':
            result += '1'
        else:
            result += '0'
    print(result)

if __name__ == "__main__":
    main()
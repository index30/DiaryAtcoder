import re

def main():
    S = input()
    r = re.compile("([a-zA-Z])([0-9]{6})([a-zA-Z])")
    m = r.match(S)
    if m:
        if len(str(int(m.groups()[1]))) == 6:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == "__main__":
    main()
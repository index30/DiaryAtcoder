def main():
    S = input()
    T = input()
    if len(S) > len(T):
        print("No")
    else:
        out_count = 0
        for s, t in zip(S, T):
            if s != t:
                out_count += 1
    
        if out_count == 0:
            print("Yes")
        else:
            print("No")

    
if __name__ == "__main__":
    main()
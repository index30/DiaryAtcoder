def main():
    A, B, C, D, E, F = list(map(int, input().split()))
    tmp1 = ((A*B*C)-(D*E*F))%998244353
    print(tmp1)
 
if __name__ == "__main__":
    main()
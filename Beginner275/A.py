import numpy as np

def main():
    _ = int(input())
    H_list = list(map(int, input().split()))
    print(np.argmax(H_list)+1)

if __name__ == "__main__":
    main()
def main():
    N, M = list(map(int, input().split()))
    a_list = list(map(int, input().split()))

    horyu = []
    result = ""
    for i in range(N):
        if (i+1) in a_list:
            horyu = [i+1] + horyu
        else:
            if len(horyu) == 1:
                tmp = f'{horyu[0]} '
            elif len(horyu) > 1:
                tmp = " ".join(map(str, horyu)) + " "
            else:
                tmp = ""
            horyu = []
            result += f'{i+1} ' + tmp
            
    print(result)

if __name__ == "__main__":
    main()
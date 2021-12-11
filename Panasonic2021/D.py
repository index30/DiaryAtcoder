# WIP

def main():
    N, M = list(map(int, input().split()))
    N_dict = {n: {} for n in range(1, N+1)}
    AB_tuple_list = [tuple(map(int, input().split())) for _ in range(M)]
    print(AB_tuple_list)


if __name__ == "__main__":
    main()

import itertools

def calc_dist(p1, p2):
    dist_val = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
    return dist_val

def main():
    N = int(input())
    pos_list = []
    for _ in range(N):
        x, y = list(map(int, input().split()))
        pos_list.append((x, y))
    
    pm = itertools.permutations(pos_list, N)
    comb_count = 0
    sum_dist = 0

    for pos_tuple in pm:
        comb_count += 1
        for i in range(len(pos_tuple)-1):
            sum_dist += calc_dist(pos_tuple[i], pos_tuple[i+1])

    print(sum_dist/comb_count)


if __name__ == "__main__":
    main()
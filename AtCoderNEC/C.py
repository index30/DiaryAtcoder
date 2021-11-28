# 時間が足りず時間内提出は不可
def main():
    N, W = list(map(int, input().split()))
    pizza_list = [list(map(int, input().split())) for _ in range(N)]
    sorted_pizza = sorted(pizza_list, key=lambda x: x[0])[::-1]
    sum_oishi, sum_weight, weight_ind = 0, 0, 0
    while (sum_weight <= W) and (weight_ind <= len(pizza_list)-1):
        if sum_weight + sorted_pizza[weight_ind][1] > W:
            sum_oishi += sorted_pizza[weight_ind][0] * (W - sum_weight)
            sum_weight += W - sum_weight
            break
        else:
            sum_weight += sorted_pizza[weight_ind][1]
            sum_oishi += sorted_pizza[weight_ind][0] * \
                sorted_pizza[weight_ind][1]
        weight_ind += 1
    print(sum_oishi)


if __name__ == "__main__":
    main()

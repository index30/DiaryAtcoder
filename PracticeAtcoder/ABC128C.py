def main():
    # 入力受付
    N, M = list(map(int, input().split()))
    switch_list = []
    for _ in range(M):
        tmp_list = list(map(int, input().split()))
        switch_list.append(tmp_list)
    p_list = list(map(int, input().split()))
    # 出力
    target_count = 0

    # スイッチの状態をbitで表す
    for bit in range(1 << N):
        light_count = 0
        for i, switchs in enumerate(switch_list):
            count = 0
            s_list = switchs[1:]
            for s in s_list:
                mask = 1 << (s-1)
                if bit&mask:
                    count += 1
            # print(bit, switchs, count, count % 2)
            if count % 2 == p_list[i]:
                light_count += 1
        if light_count == M:
            target_count += 1
    
    print(target_count)


if __name__=="__main__":
    main()
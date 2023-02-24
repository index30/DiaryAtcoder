def main():
    # 入力の受け付け
    N = int(input())
    # 出力用
    target_count = 0

    for n in range(1, N+1):
        # 奇数判定
        if n % 2 != 0:
            divisor_count = 0
            for div_num in range(1, n+1):
                if n % div_num == 0:
                    divisor_count += 1
            if divisor_count == 8:
                target_count += 1
        else:
            continue

    print(target_count)

if __name__ == "__main__":
    main()
import copy


def calc_bomb(grid, H, W):
    bomb_grid = copy.deepcopy(grid)
    for i in range(H):
        for j in range(W):
            bomb_grid[i][j] = 0

    for i in range(1, H):
        for j in range(W-1):
            if grid[i-1][j+1] == '#':
                bomb_grid[i][j] += 1

    for i in range(H-1):
        for j in range(1, W):
            if grid[i+1][j-1] == '#':
                bomb_grid[i][j] += 1

    for i in range(H-1):
        for j in range(W-1):
            if grid[i+1][j+1] == '#':
                bomb_grid[i][j] += 1

    for i in range(H-1):
        for j in range(W):
            if grid[i+1][j] == '#':
                bomb_grid[i][j] += 1

    for i in range(H):
        for j in range(W-1):
            if grid[i][j+1] == '#':
                bomb_grid[i][j] += 1

    for i in range(1, H):
        for j in range(1, W):
            if grid[i-1][j-1] == '#':
                bomb_grid[i][j] += 1

    for i in range(1, H):
        for j in range(W):
            if grid[i-1][j] == '#':
                bomb_grid[i][j] += 1

    for i in range(H):
        for j in range(1, W):
            if grid[i][j-1] == '#':
                bomb_grid[i][j] += 1

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                bomb_grid[i][j] = "#"

    return bomb_grid


def print_grid(grid):
    for g in grid:
        print("".join(map(str, g)))


def main():
    H, W = list(map(int, input().split()))
    S_list = [list(input()) for _ in range(H)]
    bomb_gird = calc_bomb(S_list, H, W)
    print_grid(bomb_gird)


if __name__ == "__main__":
    main()

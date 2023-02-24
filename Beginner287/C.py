def main():
    N, M = list(map(int, input().split()))
    matrix = [[0]*N for _ in range(N)]
    S_list, T_list = [], []
    edge = {}
    if M == 0:
        print("No")
    else:
        for _ in range(M):
            u, v = list(map(int, input().split()))
            if not edge.get(u-1):
                edge[u-1] = []
            if not edge.get(v-1):
                edge[v-1] = []
            edge[u-1].append(v-1)
            edge[v-1].append(u-1)
            matrix[u-1][v-1] = 1
            matrix[v-1][u-1] = 1
        
        # 深さ優先探索ですべての頂点が連結されているか判定

        def dfs_1(v):
            # 頂点 v を訪問済みにする
            visited[v] = 1
            for v2 in range(N):
                # 頂点 v と頂点 v2 との結合が無い場合
                if matrix[v][v2] == 0:
                    continue
                # v2 は訪問済みの場合
                if visited[v2] == 1:
                    continue
                dfs_1(v2)

        # 訪問履歴
        visited = [0] * N
        # 頂点visited[start]を始点とし、各頂点を可能な限り訪問する
        dfs_1(0)
        # print(matrix)
        # print(visited)

        # 終点に訪問したかどうか判定
        if visited[-1]!=1:
            print("No")
        else:
            # 遷移元の頂点
            parent=[-1]*N
            # 閉路に含まれる辺の集合
            loop =set()
            # 既に探索した頂点か
            come=[False]*N

            def dfs(x,last=-1):
                if last!=-1:
                    parent[x]=last
                come[x]=True
                for i in edge[x]:
                    if i ==last:continue
                    if come[i]:
                        now=x
                        loop.add((now,i))
                        loop.add((i,now))
                        while now!=i:
                            loop.add((now,parent[now]))
                            loop.add((parent[now],now))
                            now=parent[now]
                        return True
                    else:
                        if dfs(i,x):
                            return True
                return False

            if dfs(0):
                print("No")
            else:
                print("Yes")

if __name__ == "__main__":
    main()
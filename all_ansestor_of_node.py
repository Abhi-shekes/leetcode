class Solution:
    def getAncestors(self, n, edges) :
        map = [set() for _ in range(n)]
        res = [[] for _ in range(n)]
        visited = [False] * n

        def dfs(v, p):
            visited[v] = True
            if v != p:
                res[v].append(p)
            for x in map[v]:
                if not visited[x]:
                    dfs(x, p)

        for u, v in edges:
            map[u].add(v)

        for i in range(n):
            visited = [False] * n
            dfs(i, i)

        return res
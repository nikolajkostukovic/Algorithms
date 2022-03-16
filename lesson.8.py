
class Solution:
    def makeConnected(self, n: int, connection: list[list[int]]) -> int:
        def dfs(visited, adj_list,node):
            stack = [node]
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    if i not in visited:
                        stack.append(i)
                        


        if len(connection) < n -1: return - 1

        adj_lst = [[] for i in range(n)]
        for i in connection:
            adj_lst[i[0]].append(i[1])
            adj_lst[i[1]].append(i[0])

        visited = set()
        disconnected_cnt = 0
        for i in range(n):
            if i not in visited:
                disconnected_cnt += 1
                dfs(visited,adj_lst, i)
        return disconnected_cnt -1


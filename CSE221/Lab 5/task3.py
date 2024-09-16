# task 3

def dfs(adj_lst, node):
    visited_arr[node] = 0  # visited
    print(node, end=" ", file=output_file)

    for adj in adj_lst[node]:
        if visited_arr[adj] == -1:  # visit only when unvisited
            dfs(adj_lst, adj)

    visited_arr[node] = 1  # explored


input_file = open("input3_4.txt", "r")
output_file = open("output3_4.txt", 'w')

n, m = list(map(int, input_file.readline().split()))
adj_lst = {}
visited_arr = [-1] * (n + 1)
# -1 = unvisited node
# 0 = visited but not explored
# 1 = visited and explored

for i in range(n + 1):
    adj_lst[i] = []

for edge_no in range(m):
    u, v = list(map(int, input_file.readline().split()))

    adj_lst[u].append(v)
    adj_lst[v].append(u)

dfs(adj_lst, 1)
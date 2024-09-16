# task 2

def dfs(adj_lst, node, visit_arr):
    visited_arr[node] = 0  # visited
    count = 1

    for adj in adj_lst[node]:
        if visit_arr[adj] == -1:  # visit only when unvisited
            count += dfs(adj_lst, adj, visit_arr)

    visited_arr[node] = 1  # explored
    return count


input_file = open("input2b.txt", "r")
output_file = open("output2b.txt", 'w')

n, k = list(map(int, input_file.readline().split()))

adj_lst = {}
for i in range(n):
    adj_lst[i] = []

for edge_no in range(k):
    visited_arr = [-1] * n
    # -1 = unvisited node
    # 0 = visited but not explored
    # 1 = visited and explored

    u, v = list(map(int, input_file.readline().split()))

    adj_lst[u].append(v)
    adj_lst[v].append(u)

    joined = dfs(adj_lst, u, visited_arr)
    print(joined, file = output_file)

input_file.close()
output_file.close()
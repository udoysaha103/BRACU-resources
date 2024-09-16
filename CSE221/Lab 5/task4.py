# task 4

def dfs(adj_lst, node):
    visited_arr[node] = 0  # visited
    ans = False

    for adj in adj_lst[node]:
        if visited_arr[adj] == -1:  # visit only when unvisited
            ans = ans or dfs(adj_lst, adj)
        elif visited_arr[adj] == 0:  # already under exploration; cycle detected
            return True
        elif visited_arr[adj] == 1:  # explored; won't consider now
            continue

    visited_arr[node] = 1  # explored
    return ans or False


input_file = open("input4_5.txt", "r")
output_file = open("output4_5.txt", 'w')

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

if dfs(adj_lst, 1) == True:
    print("YES", file=output_file)
else:
    print("No", file=output_file)

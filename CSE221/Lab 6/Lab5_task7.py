# task 7

from queue import Queue


def bfs(adj_lst, start):
    visited_arr = [-1] * len(adj_lst)
    parent_arr = [-1] * len(adj_lst)
    length_arr = [-1] * len(adj_lst)
    # -1 = unvisited node
    # 0 = visited but not explored
    # 1 = visited and explored
    que = Queue()
    que.put(start)
    visited_arr[start] = 0
    length_arr[start] = 0

    while not que.empty():
        u = que.get()
        visited_arr[u] = 1

        for v in adj_lst[u]:
            if visited_arr[v] == -1:  # enqueue only when unvisited
                que.put(v)
                visited_arr[v] = 0
                parent_arr[v] = u
                length_arr[v] = length_arr[u] + 1

    return length_arr


input_file = open("Lab5_task7_input2.txt", "r")
output_file = open("Lab5_task7_output2.txt", "w")


n = int(input_file.readline())
adj_lst = {}
for i in range(n + 1):
    adj_lst[i] = []

for edge_no in range(n-1):
    u, v = list(map(int, input_file.readline().split()))

    adj_lst[u].append(v)
    adj_lst[v].append(u)


length_arr = []
length = 0

for u in range(1, n+1):
  current_length_arr = bfs(adj_lst, u)
  current_length = max(current_length_arr)

  if current_length > length:
    length_arr = current_length_arr
    length = current_length


print(length_arr.index(0), length_arr.index(length), file=output_file)
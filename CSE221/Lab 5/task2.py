# task 2

from queue import Queue

def bfs(adj_lst, start):
  visited_arr = [-1] * len(adj_lst)
  # -1 = unvisited node
  # 0 = visited but not explored
  # 1 = visited and explored
  que = Queue()
  que.put(start)
  visited_arr[start] = 0

  while not que.empty():
    u = que.get()
    visited_arr[u] = 1
    print(u, end = " ", file = output_file)

    for v in adj_lst[u]:
      if visited_arr[v] == -1:  # enqueue only when unvisited
        que.put(v)
        visited_arr[v] = 0


input_file = open("input2_4.txt", "r")
output_file = open("output2_4.txt", 'w')

n, m = list(map(int, input_file.readline().split()))
adj_lst = {}
for i in range(n+1):
  adj_lst[i] = []

for edge_no in range(m):
  u, v = list(map(int, input_file.readline().split()))

  adj_lst[u].append(v)
  adj_lst[v].append(u)

bfs(adj_lst, 1)
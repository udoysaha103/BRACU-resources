# task 1

from queue import Queue


def Dijkstra(adj_lst, start):
    visited_arr = [-1] * (len(adj_lst))
    length_arr = [-1] * (len(adj_lst))
    # -1 = Unvisited
    # 0 = Visited but Not Explored
    # 1 = Visited and Explored
    que = Queue()
    que.put(start)
    visited_arr[start] = 0
    length_arr[start] = 0

    while not que.empty():
        u = que.get()
        visited_arr[u] = 1  # visited

        for distance in sorted(list(adj_lst[u].keys())):
            adjacents = adj_lst[u][distance]

            for node in adjacents:
                if visited_arr[node] == -1:  # unvisited
                    que.put(node)
                    visited_arr[node] = 0
                    length_arr[node] = length_arr[u] + distance
                elif visited_arr[node] == 0:  # visited but not explored
                    if (length_arr[u] + distance) < length_arr[node]:
                        length_arr[node] = length_arr[u] + distance
                else:
                    continue

    return length_arr


input_file = open("input1_1.txt", "r")
output_file = open("output1_1.txt", 'w')

n, m = list(map(int, input_file.readline().split()))
adj_lst = {}
for i in range(n + 1):
    adj_lst[i] = dict()

for edge_no in range(m):
    u, v, w = list(map(int, input_file.readline().split()))

    if w not in adj_lst[u]:
        adj_lst[u][w] = [v]
    else:
        adj_lst[u][w].append(v)

start = int(input_file.readline())

length_arr = Dijkstra(adj_lst, start)
print(" ".join(map(str, length_arr[1:])), file=output_file)
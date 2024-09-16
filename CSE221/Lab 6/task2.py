# task 2

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


input_file = open("input2_2.txt", "r")
output_file = open("output2_2.txt", "w")

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

start1, start2 = list(map(int, input_file.readline().split()))

length_arr_1 = Dijkstra(adj_lst, start1)
length_arr_2 = Dijkstra(adj_lst, start2)

maximum_time = -1
node = -1

for i in range(1, n + 1):
    if length_arr_1[i] >= 0 and length_arr_2[i] >= 0:
        if maximum_time == -1:
            maximum_time = max(length_arr_1[i], length_arr_2[i])
            node = i
        else:
            m = max(length_arr_1[i], length_arr_2[i])

            if m < maximum_time:
                maximum_time = m
                node = i

if node == -1:
    print("Impossible", file=output_file)
else:
    print("Time", maximum_time, file=output_file)
    print("Node", node, file=output_file)
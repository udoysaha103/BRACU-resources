# task 3

import heapq

def prim(adj_lst, start):
    visited_arr = [-1] * (len(adj_lst))
    weight_arr = [-1] * (len(adj_lst))
    # -1 = Unvisited
    # 0 = Visited but Not Explored
    # 1 = Visited and Explored
    weight_arr[start] = [0, start, -1]  # items are in the format (cost, self, parent)
    visited_arr[start] = 0
    heap = []
    heapq.heappush(heap, weight_arr[start])

    while len(heap) > 0:
        u = heapq.heappop(heap)[1]
        visited_arr[u] = 1

        for v, w in adj_lst[u]:
            if visited_arr[v] == -1:  # unvisited
                visited_arr[v] = 0
                weight_arr[v] = [w, v, u]

                heapq.heappush(heap, weight_arr[v])
            elif visited_arr[v] == 0:  # in queue
                if w < weight_arr[v][0]:
                    weight_arr[v][0] = w
                    weight_arr[v][2] = u

                    heapq.heapify(heap)

    return weight_arr


input_file = open("input3_1.txt", "r")
output_file = open("output3_1.txt", "w")

n, m = list(map(int, input_file.readline().split()))
adj_lst = {}
for i in range(n + 1):
    adj_lst[i] = []

for edge_no in range(m):
    u, v, w = list(map(int, input_file.readline().split()))

    if u == v:  # removing self loops
        continue

    edge = [v, w]

    flag = False
    for i in adj_lst[u]:  # removing parallel edges
        if i[0] == v:
            Flag = True

            if w < i[1]:
                i[1] = w

            break

    if flag == False:
        adj_lst[u].append(edge)

mst_edges = prim(adj_lst, 1)

maximum_edge_weight = 0
for w, v, u in mst_edges[1: ]:
    if w > maximum_edge_weight:
        maximum_edge_weight = w

print(maximum_edge_weight, file=output_file)
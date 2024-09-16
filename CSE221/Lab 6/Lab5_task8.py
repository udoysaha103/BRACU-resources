# task 8

from queue import Queue


def bfs(adj_lst, start):
    que = Queue()
    que.put(start)
    adj_lst[start][0] = 1  # coloring with 1 and 2
    color1_count = 1
    color2_count = 0

    while not que.empty():
        u = que.get()

        for v in adj_lst[u][1]:
            if adj_lst[v][0] == 0:  # enqueue only when unvisited
                que.put(v)

                if adj_lst[u][0] == 1:
                    adj_lst[v][0] = 2
                    color2_count += 1
                else:
                    adj_lst[v][0] = 1
                    color1_count += 1

    return max(color1_count, color2_count)


input_file = open("Lab5_task8_input0.txt", "r")
output_file = open("Lab5_task8_output0.txt", "w")

test_cases = int(input_file.readline())

for case in range(test_cases):
    m = int(input_file.readline())
    adj_lst = {}

    for edge_no in range(m):
        u, v = list(map(int, input_file.readline().split()))

        if u not in adj_lst:
            adj_lst[u] = [0, [v]]
        else:
            adj_lst[u][1].append(v)

        if v not in adj_lst:
            adj_lst[v] = [0, [u]]
        else:
            adj_lst[v][1].append(u)

    print(f"Case {case+1}:", bfs(adj_lst, list(adj_lst.keys())[0]), file=output_file)

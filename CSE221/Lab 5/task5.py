# task 5

from queue import Queue


def bfs(adj_lst, start):  # bfs is level order traversal, so it can be used to find the shortest distance
    visited_arr = [-1] * len(adj_lst)
    parent_arr = [-1] * len(adj_lst)
    # -1 = unvisited node
    # 0 = visited but not explored
    # 1 = visited and explored
    que = Queue()
    que.put(start)
    visited_arr[start] = 0

    while not que.empty():
        u = que.get()
        visited_arr[u] = 1

        for v in adj_lst[u]:
            if visited_arr[v] == -1:  # enqueue only when unvisited
                que.put(v)
                visited_arr[v] = 0
                parent_arr[v] = u

    return parent_arr


input_file = open("input5_5.txt", "r")
output_file = open("output5_5.txt", 'w')

n, m, d = list(map(int, input_file.readline().split()))
adj_lst = {}
for i in range(n + 1):
    adj_lst[i] = []

for edge_no in range(m):
    u, v = list(map(int, input_file.readline().split()))

    adj_lst[u].append(v)
    adj_lst[v].append(u)

parent_arr = bfs(adj_lst, 1)  # gets the parent array, starting from the source

path_stack = []  # a stack to define the path
current_node = d
while current_node != 1:  # making the path stack
    path_stack.append(current_node)
    current_node = parent_arr[current_node]

print("Time:", len(path_stack), file = output_file)
print("Shortest Path: 1", end = "", file = output_file)
while len(path_stack) != 0:  # fetching the actual path, starting with source = 1
    print("", path_stack.pop(), end = "", file = output_file)
print("", file = output_file)
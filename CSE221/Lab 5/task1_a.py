# task 1 (A)

input_file = open("input1_a_2.txt", "r")
output_file = open("output1_a_2.txt", 'w')

n, m = list(map(int, input_file.readline().split()))
adj_mat = [[0 for i in range(n + 1)] for j in range(n + 1)]

for edge_no in range(m):
    u, v, w = list(map(int, input_file.readline().split()))

    adj_mat[u][v] = w

for u in range(n + 1):
    print(" ".join(map(str, adj_mat[u])), file=output_file)

input_file.close()
output_file.close()

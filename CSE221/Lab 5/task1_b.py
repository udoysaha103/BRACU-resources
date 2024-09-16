# task 1 (B)

input_file = open("input1_b_3.txt", "r")
output_file = open("output1_b_3.txt", 'w')

n, m = list(map(int, input_file.readline().split()))
adj_lst = {}
for i in range(n + 1):
    adj_lst[i] = []

for edge_no in range(m):
    u, v, w = list(map(int, input_file.readline().split()))

    adj_lst[u].append((v, w))

for u in range(n + 1):
    print(u, ":", " ".join(map(str, adj_lst[u])), file=output_file)

input_file.close()
output_file.close()

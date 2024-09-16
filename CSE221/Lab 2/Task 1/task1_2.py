# task 1 (2)

input_file = open("input1_4.txt", mode = "r")
output_file = open("output1_4.txt", mode = 'w')

n, s = list(map(int, input_file.readline().split()))
arr = list(map(int, input_file.readline().split()))

dic1 = {}

flag = 0
for i in range(n):
  if s - arr[i] not in dic1:
    dic1[arr[i]] = i
  else:
    flag = 1
    print(dic1[s - arr[i]] + 1, i + 1, file = output_file)
    break

if flag == 0:
  print("IMPOSSIBLE", file = output_file)

input_file.close()
output_file.close()
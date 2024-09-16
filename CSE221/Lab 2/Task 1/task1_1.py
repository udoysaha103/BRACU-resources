# task 1 (1)

input_file = open("input1_4.txt", mode = "r")
output_file = open("output1_4.txt", mode = 'w')

n, s = list(map(int, input_file.readline().split()))
arr = list(map(int, input_file.readline().split()))

flag = 0
for i in range(n - 1):
  for j in range(i + 1, n):
    if arr[i] + arr[j] == s:
      print(i+1, j+1, file = output_file)
      flag = 1
      break
  if flag == 1:
    break

if flag == 0:
  print("IMPOSSIBLE", file = output_file)

input_file.close()
output_file.close()
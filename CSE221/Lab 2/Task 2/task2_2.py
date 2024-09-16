# task 2 (2)
# using two pointer method to implement O(n) solution

input_file = open("input2_4.txt", mode = "r")
output_file = open("output2_4.txt", mode = 'w')

n = int(input_file.readline())
alice = list(map(int, input_file.readline().split()))

m = int(input_file.readline())
bob = list(map(int, input_file.readline().split()))

combined_list = []

i1 = i2 = 0

while i1 < n and i2 < m:
  if alice[i1] < bob[i2]:
    combined_list.append(alice[i1])
    i1 += 1
  else:
    combined_list.append(bob[i2])
    i2 += 1

while i1 < n:
  combined_list.append(alice[i1])
  i1 += 1

while i2 < m:
  combined_list.append(bob[i2])
  i2 += 1

print(" ".join(map(str, combined_list)), file = output_file)

input_file.close()
output_file.close()
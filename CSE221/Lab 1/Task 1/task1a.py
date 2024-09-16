# task 1 (a)

input_file = open("input1a.txt", mode = 'r')
output_file = open("output1a.txt", mode = 'w')

t = int(input_file.readline())

for i in range(t):
  n = int(input_file.readline())
  if n % 2 == 0:
    print(f"{n} is an Even number.", file = output_file)
  else:
    print(f"{n} is an Odd number.", file = output_file)

input_file.close()
output_file.close()
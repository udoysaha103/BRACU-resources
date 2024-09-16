# task 1 (b)

input_file = open("input1b.txt", mode = 'r')
output_file = open("output1b.txt", mode = 'w')

t = int(input_file.readline())

for i in range(t):
  arr = input_file.readline().split()
  oprnd1 = int(arr[1])
  operator = arr[2]
  oprnd2 = int(arr[3])

  if operator == '+':
    print(f"The result of {oprnd1} {operator} {oprnd2} is {oprnd1 + oprnd2}", file = output_file)
  elif operator == '-':
    print(f"The result of {oprnd1} {operator} {oprnd2} is {oprnd1 - oprnd2}", file = output_file)
  elif operator == '*':
    print(f"The result of {oprnd1} {operator} {oprnd2} is {oprnd1 * oprnd2}", file = output_file)
  elif operator == '/':
    print(f"The result of {oprnd1} {operator} {oprnd2} is {oprnd1 / oprnd2}", file = output_file)

input_file.close()
output_file.close()
# task 4

input_file = open("input4d.txt", "r")
output_file = open("output4d.txt", 'w')

n = int(input_file.readline())

if n < 3:
    print(n, file = output_file)
else:
    i = 0
    j = 1

    for k in range(n):
        i, j = j, i+j

    print(j, file = output_file)

input_file.close()
output_file.close()
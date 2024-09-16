# task 1

input_file = open("input1c.txt", 'r')
output_file = open("output1c.txt", 'w')

arr = []
n = int(input_file.readline())
for i in range(n):
    start, end = list(map(int, input_file.readline().split()))
    arr.append((end, start))

arr.sort()
current_time = 0

i = 0
while i < len(arr):
    if arr[i][1] >= current_time:
        current_time = arr[i][0]
        i += 1
    else:
        arr.pop(i)

print(len(arr), file = output_file)
for end, start in arr:
    print(start, end, file = output_file)

input_file.close()
output_file.close()
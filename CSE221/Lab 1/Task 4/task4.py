# task 4

def selection_sort(n, s_id, marks):
    for i in range(n - 1):
        max_index = i

        for j in range(i + 1, n):
            if marks[max_index] == marks[j]:
                if s_id[i] > s_id[j]:
                    max_index = j
            elif marks[max_index] < marks[j]:
                max_index = j

        if max_index != i:
            s_id[i], s_id[max_index] = s_id[max_index], s_id[i]
            marks[i], marks[max_index] = marks[max_index], marks[i]


input_file = open("input4.txt", mode='r')
output_file = open("output4.txt", mode='w')

n = int(input_file.readline())
s_id = list(map(int, input_file.readline().split()))
marks = list(map(int, input_file.readline().split()))

selection_sort(n, s_id, marks)

for i in range(n):
    print(f"ID: {s_id[i]} Mark: {marks[i]}", file=output_file)

input_file.close()
output_file.close()
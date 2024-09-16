# task 3

def bubbleSort(arr):
    for i in range(len(arr) - 1):
        change = 0  # keeping track of any swapping operation occured in an iteration from the beginning

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                change = 1  # change occured
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if change == 0:  # breaking the loop if no changes occurred
            break


input_file = open("input3.txt", mode='r')
output_file = open("output3.txt", mode='w')

t = int(input_file.readline())
array = list(map(int, input_file.readline().split()))

bubbleSort(array)

print(" ".join(map(str, array)), file=output_file)

input_file.close()
output_file.close()
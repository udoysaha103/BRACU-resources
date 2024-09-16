# task 3

input_file = open("input3_4.txt", mode="r")
output_file = open("output3_4.txt", mode='w')

n = int(input_file.readline())
arr = list(map(int, input_file.readline().split()))


def merge(a, b):
    # write your code here
    # Here a and b are two sorted list
    # merge function will return a sorted list after merging a and b
    merged_list = []

    i1 = i2 = 0

    while i1 < len(a) and i2 < len(b):
        if a[i1] < b[i2]:
            merged_list.append(a[i1])
            i1 += 1
        else:
            merged_list.append(b[i2])
            i2 += 1

    while i1 < len(a):
        merged_list.append(a[i1])
        i1 += 1

    while i2 < len(b):
        merged_list.append(b[i2])
        i2 += 1

    return merged_list


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[: mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)  # complete the merge function above


arr = mergeSort(arr)

print(" ".join(map(str, arr)), file=output_file)

input_file.close()
output_file.close()
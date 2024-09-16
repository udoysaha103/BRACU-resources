# task 2 (1)
# using merge-sort to implement O(n logn) solution

def merge_sort(arr, l, r):
    if l >= r:
        return

    m = (l + r) // 2
    merge_sort(arr, l, m)
    merge_sort(arr, m + 1, r)

    merge(arr, l, m, r)


def merge(arr, l, m, r):
    for index in range(m + 1, r + 1):
        element = arr[index]

        while index > l:
            if arr[index - 1] > element:
                arr[index] = arr[index - 1]
                index -= 1
            else:
                break

        arr[index] = element


input_file = open("input2_4.txt", mode="r")
output_file = open("output2_4.txt", mode='w')

n = int(input_file.readline())
alice = list(map(int, input_file.readline().split()))

m = int(input_file.readline())
bob = list(map(int, input_file.readline().split()))

combined_list = alice + bob
merge_sort(combined_list, 0, len(combined_list) - 1)

print(" ".join(map(str, combined_list)), file=output_file)

input_file.close()
output_file.close()
# task 1 (ii)

def partition(arr, low, high):
    # pivot (Element to be placed at right position)
    pivot = arr[high]
    i = (low - 1)  # larger value index
    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than the pivot
            i = i + 1  # increment index of larger value
            arr[i], arr[j] = arr[j], arr[i]  # swapping

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swapping the larger value with the pivot
    return i + 1  # returning the pivot index


def findK(arr, k, low, high):
    pi = partition(arr, low, high)

    if pi == k - 1:
        return arr[pi]
    elif pi < k - 1:
        return findK(arr, k, pi + 1, high)
    else:
        return findK(arr, k, low, pi - 1)


if __name__ == "__main__":
    input_file = open("input1b.txt", "r")
    output_file = open("output1b.txt", "w")

    arr = list(map(int, input_file.readline().split()))

    while 1:
        k = input_file.readline()

        if len(k) == 0:
            break

        k = int(k)
        print(findK(arr, k, 0, len(arr) - 1), file = output_file)
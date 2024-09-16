# task 1 (i)

# low  –> Starting index,  high  –> Ending index
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)  # Before pi
        quickSort(arr, pi + 1, high)  # After pi


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


if __name__ == "__main__":
    input_file = open("input1a.txt", "r")
    output_file = open("output1a.txt", "w")

    arr = list(map(int, input_file.readline().split()))

    quickSort(arr, 0, len(arr) - 1)

    print(" ".join(map(str, arr)), file=output_file)

    input_file.close()
    output_file.close()
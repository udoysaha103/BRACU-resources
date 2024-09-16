# task 2

def maximum_by_dnc(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_high = maximum_by_dnc(arr, low, mid)
    right_high = maximum_by_dnc(arr, mid + 1, high)

    if left_high > right_high:
        return left_high
    else:
        return right_high


if __name__ == "__main__":
    input_file = open("input2_1.txt", "r")
    output_file = open("output2_1.txt", "w")

    n = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))

    maximum = maximum_by_dnc(arr, 0, n - 1)

    print(maximum, file=output_file)

    input_file.close()
    output_file.close()
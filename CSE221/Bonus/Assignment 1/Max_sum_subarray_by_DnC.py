def cross_sum_subarray(sub_array, mid):
    left_sum = sub_array[mid - 1]
    left_sum_max = left_sum

    for i in range(mid - 2, -1, -1):
        left_sum += sub_array[i]
        if left_sum > left_sum_max:
            left_sum_max = left_sum

    right_sum = sub_array[mid]
    right_sum_max = right_sum

    for i in range(mid + 1, len(sub_array)):
        right_sum += sub_array[i]
        if right_sum > right_sum_max:
            right_sum_max = right_sum

    return left_sum_max + right_sum_max


def max_sum_subarray(sub_array):
    length = len(sub_array)

    if length == 1:  # if only one element in the array, it will return that single element
        return sub_array[0]

    mid = length // 2

    lss = max_sum_subarray(sub_array[: mid])  # left sum subarray
    rss = max_sum_subarray(sub_array[mid:])  # right sum subarray
    css = cross_sum_subarray(sub_array, mid)  # cross sum subarray

    return max((lss, css, rss))


if __name__ == "__main__":
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sum_subarray(array))

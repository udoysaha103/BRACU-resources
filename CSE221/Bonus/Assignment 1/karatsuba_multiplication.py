def karatsuba(a, b, base):  # a and b are integers, but passed as strings
    len_a = len(a)
    len_b = len(b)

    # return product of the numbers, if they are consisted of a single digit
    if len_a == 1 and len_b == 1:
        return int(a) * int(b)

    # matching lengths
    if len_a % 2 != 0:  # odd length
        a = '0' + a
        len_a += 1
    if len_b % 2 != 0:  # odd length
        b = '0' + b
        len_b += 1
    if len_a > len_b:
        b = ('0' * (len_a - len_b)) + b
    elif len_b > len_a:
        a = ('0' * (len_b - len_a)) + a

    length = len(a)
    mid = length // 2

    a_left = a[ : mid]
    a_right = a[mid: ]

    b_left = b[ : mid]
    b_right = b[mid: ]

    first_term = karatsuba(a_left, b_left, base)
    mid_sum_term = karatsuba(str(int(a_left)+int(a_right)), str(int(b_left)+int(b_right)), base)
    last_term = karatsuba(a_right, b_right, base)

    return (first_term * (base ** length)) + ((mid_sum_term - first_term - last_term) * (base ** (length // 2))) + last_term


if __name__ == "__main__":
    karat = karatsuba('5644846', '564646', 10)
    normal = 5644846 * 564646

    print(karat)
    print(normal)
    print("Matches") if karat == normal else print("Doesn't match")
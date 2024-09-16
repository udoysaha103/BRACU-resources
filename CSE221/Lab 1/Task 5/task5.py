# task 5

def lexicographic_smaller(s1, s2):
    '''
    s1 =>
    smaller : 1
    equal : 0
    larger : -1
    '''
    i1 = i2 = 0
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] < s2[i2]:
            return 1
        elif s1[i1] > s2[i2]:
            return -1

        i1 += 1
        i2 += 1

    if i1 < len(s1):
        return -1
    elif i2 < len(s2):
        return 1
    else:
        return 0

def time_compare(t1, t2):
    '''
    t1 =>
    smaller : 1
    equal : 0
    larger : -1
    '''
    h1, m1 = list(map(int, t1.split(':')))
    h2, m2 = list(map(int, t2.split(':')))

    if h1 > h2:
        return -1
    elif h1 < h2:
        return 1
    else:
        if m1 > m2:
            return -1
        elif m1 < m2:
            return 1
        else:
            return 0

def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            comparison = lexicographic_smaller(array[j][0], array[min_index][0])

            if comparison == 1:
                min_index = j
            elif comparison == 0:
                time_comparison = time_compare(array[j][2], array[min_index][2])

                if time_comparison == -1:
                    min_index = j

        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]


input_file = open("input5.txt", mode='r')
output_file = open("output5.txt", mode='w')

n = int(input_file.readline())
array = []
for line in input_file.readlines():
    line = line.split()
    array.append((line[0], line[4], line[6]))

selection_sort(array)

for train, place, time in array:
    print(f"{train} will departure for {place} at {time}", file = output_file)

input_file.close()
output_file.close()
import time
import math
import matplotlib.pyplot as plt
import numpy as np

class HospitalBubble:
    def __init__(self):
        self.queue = []

    def enque(self, name, seriousness):
        self.queue += [(seriousness, name)]
        self.sort()
        self.printQueue()

    def seeDoctor(self):
        if len(self.queue) > 0:
            patient = self.queue[0][1]
            self.queue = self.queue[1: ]
            self.printQueue()
            return patient

    def printQueue(self):
        print(self.queue)

    def sort(self):  # bubble sort
        for turn in range(len(self.queue)-1):
            flag = False

            for index in range(len(self.queue)-1):
                if self.queue[index][0] > self.queue[index + 1][0]:
                    self.queue[index], self.queue[index + 1] = self.queue[index + 1], self.queue[index]
                    flag = True

            if flag == False:
                break



class Min_Heap:
    def __init__(self, length):
        self.heap_arr = [None] * length
        self.index = 1  # index to add new value


    def add(self, val):
        if len(self.heap_arr) >= 2 and self.heap_arr[1] == None:
            self.heap_arr[1] = val
            self.index = 2
        else:
            if self.index >= len(self.heap_arr):
                height = int(math.ceil(math.log(len(self.heap_arr), 2)))
                self.heap_arr += [None] * (2 ** height)
                self.heap_arr[self.index] = val
                self.index += 1
            else:
                self.heap_arr[self.index] = val
                self.index += 1

        self.heapify(self.index - 1)


    def delete(self):
        val = None

        if self.index == 2:
            val = self.heap_arr[1]
            self.index -= 1
            self.heap_arr[self.index] = None
        elif self.index > 2:
            self.heap_arr[1], self.heap_arr[self.index - 1] = self.heap_arr[self.index - 1], self.heap_arr[1]  # swap with root
            self.index -= 1
            val = self.heap_arr[self.index]
            self.heap_arr[self.index] = None

        self.sink(1)
        return val


    def heapify(self, index):  # swim up
        while index > 1:
            if self.heap_arr[index // 2][0] > self.heap_arr[index][0]:
                self.heap_arr[index // 2], self.heap_arr[index] = self.heap_arr[index], self.heap_arr[index // 2]
                index //= 2
            else:
                break


    def sink(self, index):
        if (index * 2) + 1 < len(self.heap_arr):  # if nodes are present
            if self.heap_arr[index * 2] == None and self.heap_arr[(index * 2) + 1] == None:  # no child
                return
            elif self.heap_arr[index * 2] != None and self.heap_arr[(index * 2) + 1] != None:  # both child
                if self.heap_arr[index][0] > self.heap_arr[index * 2][0] and self.heap_arr[index][0] > self.heap_arr[(index * 2) + 1][0]:  # current root is largest
                    if self.heap_arr[index * 2][0] < self.heap_arr[(index * 2) + 1][0]:  # left child is smallest
                        self.heap_arr[index], self.heap_arr[index * 2] = self.heap_arr[index * 2], self.heap_arr[index]
                        self.sink(index * 2)
                    else:  # right child is smallest
                        self.heap_arr[index], self.heap_arr[(index * 2) + 1] = self.heap_arr[(index * 2) + 1], self.heap_arr[index]
                        self.sink((index * 2) + 1)
                elif self.heap_arr[index][0] > self.heap_arr[index * 2][0]:
                    self.heap_arr[index], self.heap_arr[index * 2] = self.heap_arr[index * 2], self.heap_arr[index]
                    self.sink(index * 2)
                elif self.heap_arr[index][0] > self.heap_arr[(index * 2) + 1][0]:
                    self.heap_arr[index], self.heap_arr[(index * 2) + 1] = self.heap_arr[(index * 2) + 1], self.heap_arr[index]
                    self.sink((index * 2) + 1)
            elif self.heap_arr[index * 2] != None:  # left child
                if self.heap_arr[index][0] > self.heap_arr[index * 2][0]:
                    self.heap_arr[index], self.heap_arr[index * 2] = self.heap_arr[index * 2], self.heap_arr[index]
                    self.sink(index * 2)


    def __str__(self):
        return str(self.heap_arr)



class HospitalHeap:
    def __init__(self):
        self.queue = Min_Heap(1)

    def enque(self, name, seriousness):
        self.queue.add((seriousness, name))
        self.printQueue()

    def seeDoctor(self):
        patient = self.queue.delete()
        self.printQueue()
        return patient[1]

    def printQueue(self):
        print(self.queue)


if __name__ == "__main__":
    input_file = open("input3.txt", "r")
    offset = time.time()
    data = input_file.readlines()
    print(data)
    offset = time.time() - offset

    n = len(data)

    x = [i for i in range(n)]
    y = [0 for i in range(n)]
    z = [0 for i in range(n)]

    i = 0
    start = time.time()
    hospital = HospitalBubble()
    for line in data:
        if line[-1] == '\n':
            line = line[: -1]

        if line.lower() == "see doctor":
            patient = hospital.seeDoctor()
        else:
            hospital.enque(line[: -2], int(line[-1]))

        y[i] = time.time() - start + offset
        i += 1

    i = 0
    start = time.time()
    hospital = HospitalHeap()
    for line in data:
        if line[-1] == '\n':
            line = line[: -1]

        if line.lower() == "see doctor":
            patient = hospital.seeDoctor()
        else:
            hospital.enque(line[: -2], int(line[-1]))

        z[i] = time.time() - start + offset
        i += 1

    x_interval = math.ceil(n / 10)
    plt.plot(x, y, 'r')  # bubble
    plt.plot(x, z, 'b')  # heap
    plt.xticks(np.arange(min(x), max(x) + 1, x_interval))
    plt.xlabel('n-th data')
    plt.ylabel('time')
    plt.title('Comparing Time Complexity!')
    plt.show()

    print(x, "\n", y, "\n", z)

    input_file.close()
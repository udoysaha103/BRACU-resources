import math

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


class Hospital:
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
    output_file = open("output3_heap_sort.txt", "w")

    hospital = Hospital()

    for line in input_file.readlines():
        if line[-1] == '\n':
            line = line[: -1]

        if line.lower() == "see doctor":
            patient = hospital.seeDoctor()
            print(patient, file = output_file)
        else:
            hospital.enque(line[: -2], int(line[-1]))

    input_file.close()
    output_file.close()
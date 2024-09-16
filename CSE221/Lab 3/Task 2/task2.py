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


    def build(self, data):
        for element in data:
            self.add(element)

        print(self)


    def heapify(self, index):  # swim up
        while index > 1:
            if self.heap_arr[index // 2] > self.heap_arr[index]:
                self.heap_arr[index // 2], self.heap_arr[index] = self.heap_arr[index], self.heap_arr[index // 2]
                index //= 2
            else:
                break


    def sink(self, index):
        if (index * 2) + 1 < len(self.heap_arr):  # if nodes are present
            if self.heap_arr[index * 2] == None and self.heap_arr[(index * 2) + 1] == None:  # no child
                return
            elif self.heap_arr[index * 2] != None and self.heap_arr[(index * 2) + 1] != None:  # both child
                if self.heap_arr[index] > self.heap_arr[index * 2] and self.heap_arr[index] > self.heap_arr[(index * 2) + 1]:  # current root is largest
                    if self.heap_arr[index * 2] < self.heap_arr[(index * 2) + 1]:  # left child is smallest
                        self.heap_arr[index], self.heap_arr[index * 2] = self.heap_arr[index * 2], self.heap_arr[index]
                        self.sink(index * 2)
                    else:  # right child is smallest
                        self.heap_arr[index], self.heap_arr[(index * 2) + 1] = self.heap_arr[(index * 2) + 1], self.heap_arr[index]
                        self.sink((index * 2) + 1)
                elif self.heap_arr[index] > self.heap_arr[index * 2]:
                    self.heap_arr[index], self.heap_arr[index * 2] = self.heap_arr[index * 2], self.heap_arr[index]
                    self.sink(index * 2)
                elif self.heap_arr[index] > self.heap_arr[(index * 2) + 1]:
                    self.heap_arr[index], self.heap_arr[(index * 2) + 1] = self.heap_arr[(index * 2) + 1], self.heap_arr[index]
                    self.sink((index * 2) + 1)
            elif self.heap_arr[index * 2] != None:  # left child
                if self.heap_arr[index] > self.heap_arr[index * 2]:
                    self.heap_arr[index], self.heap_arr[index * 2] = self.heap_arr[index * 2], self.heap_arr[index]
                    self.sink(index * 2)


    def heapSort(self):
        sorted_arr = [None] * (self.index - 1)
        i = 0

        while self.index > 1:
            sorted_arr[i] = self.delete()
            i += 1

        return sorted_arr


    def __str__(self):
        return str(self.heap_arr)


if __name__ == "__main__":
    input_file = open("input2.txt", "r")
    output_file = open("output2.txt", "w")

    data = list(map(int, input_file.readline().split()))

    heap = Min_Heap(2 ** int(math.ceil(math.log(len(data), 2))))
    heap.build(data)

    print("Change in heap =>\n", file = output_file)

    while 1:
        user_input = input("‘A’: for Adding a new number\n‘B’: for Deleting\n‘S’: for Sorting\n'E': for EXIT\nEnter your choice => ")
        if user_input.lower() == 'e':
            break
        elif user_input.lower() == 'a':
            heap.add(int(input("Enter the value (integer): ")))
        elif user_input.lower() == 'b':
            heap.delete()
        elif user_input.lower() == 's':
            sorted_arr = heap.heapSort()
            print(sorted_arr)
            print("After sorting : ", sorted_arr, file = output_file)
        else:
            print("!!!!!Wrong choice!!!!!\n\n")
            continue

        print(heap, "\n\n")
        print(heap, '\n', file = output_file)

    input_file.close()
    output_file.close()
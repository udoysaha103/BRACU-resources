class Hospital:
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

if __name__ == "__main__":
    input_file = open("input3.txt", "r")
    output_file = open("output3_bubble_sort.txt", "w")

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
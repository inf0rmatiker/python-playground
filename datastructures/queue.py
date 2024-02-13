
class Queue:

    def __init__(self):
        self.array = []

    def size(self):
        return len(self.array)

    def print(self):
        print(self.array)

    def offer(self, item):
        self.array.append(item)

    def poll(self):
        if len(self.array) == 0:
            return -1, False
        item = self.array[0]
        self.array = self.array[1:]
        return item, True

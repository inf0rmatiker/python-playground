
class Stack:

    def __init__(self):
        self.array = []


    def __len__(self):
        return len(self.array)

    def size(self) -> int:
        return len(self.array)

    def print(self):
        print(self.array)

    def push(self, item):
        self.array.append(item)

    def pop(self):
        if len(self.array) == 0:
            return -1, False
        last = self.array[-1]
        self.array = self.array[:-1]
        return last
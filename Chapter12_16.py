# 12.16 Write a test program that prompts the user to enter five strings and
# displays them in reverse order


class Stack(list):

    def __init__(self):
        super().__init__()

    def isEmpty(self):
        return self.__len__() == 0

    def peek(self):
        return self.__getitem__(len(self) - 1)

    def push(self, value):
        self.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return list.pop(self)

    def getSize(self):
        return len(self)


def main():
    stack1 = Stack()

    print("Enter five strings: ")
    for i in range(0, 5):
        stack1.push(input())

    while not stack1.isEmpty():
        print(stack1.pop(), end = " ")


main()

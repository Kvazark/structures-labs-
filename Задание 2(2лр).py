class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class Stack:

    def __init__(self, elements):
        self.head = None
        if elements is not None:
            for e in elements:
                self.push(e)
        pass

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            current = Node(val)
            current.next = self.head
            self.head = current

    def pop(self):
        value = self.head.val
        self.head = self.head.next
        return value

    def __str__(self):
        ret = "["
        current = self.head

        while current is not None:
            ret += current.val.__str__() + ", "
            current = current.next

        return ret + "]"


class Queue:

    def __init__(self, elements):
        self.head = None
        self.last = None
        if elements is not None:
            for e in elements:
                self.enqueue(e)
        pass

    def enqueue(self, val):
        if self.head is None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last.next = Node(val)
            self.last = self.last.next

    def dequeue(self):
        if self.head is not None:
            value = self.head.val
            self.head = self.head.next
            return value

    def __str__(self):
        ret = "["
        current = self.head

        while current is not None:
            ret += current.val.__str__() + ", "
            current = current.next

        return ret + "]"


queue1 = Queue(None)
queue2 = Queue(None)
stack = Stack(None)


def seed_data():
    print("Введите начальные элементы очереди 1: ", end="")
    for e in list(map(int, input().split())):
        queue1.enqueue(e)

    print("Введите начальные элементы очереди 2: ", end="")
    for e in list(map(int, input().split())):
        queue2.enqueue(e)

    print("Введите начальные элементы стека: ", end="")
    for e in list(map(int, input().split())):
        stack.push(e)


def main():
    global queue1, queue2, stack

    print("Хотите заполнить структуры заранее? (y): ", end="")
    if input().lower() == "y":
        seed_data()

    while True:
        print("Выберите структуру для обработки (q1, q2, s): ", end="")

        structure = input()

        if structure != "q1" and structure != "q2" and structure != "s":
            break

        print("1. Вставка\n"
              "2. Удаление\n"
              "3. Просмотр\n")
        command = int(input())

        if command == 1:
            if structure == "q1":
                print("Введите значение: ", end="")
                val = int(input())
                queue1.enqueue(val)
            elif structure == "q2":
                print("Введите значение: ", end="")
                val = int(input())
                queue2.enqueue(val)
            else:
                print("Введите значение: ", end="")
                val = int(input())
                stack.push(val)
            pass
        elif command == 2:
            if structure == "q1":
                queue1.dequeue()
            elif structure == "q2":
                queue2.dequeue()
            else:
                stack.pop()
            pass
        elif command == 3:
            if structure == "q1":
                print(queue1)
            elif structure == "q2":
                print(queue2)
            else:
                print(stack)
            pass


if __name__ == "__main__":
    main()

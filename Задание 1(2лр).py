class DynamicArray:
    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def add(self, element):
        self.elements.append(element)

    def remove_at(self, index):
        self.elements.pop(index)

    def insert(self, index, val):
        self.elements.insert(index, val)

    def get(self, index):
        return self.elements[index]

    def __str__(self):
        ret = "["

        for e in self.elements:
            ret += e.__str__() + ", "

        return ret + "]"


class Queue:
    def __init__(self):
        self.inner_array = DynamicArray()
        pass

    def enqueue(self, val):
        self.inner_array.add(val)

    def dequeue(self):
        if self.inner_array.size() > 0:
            val = self.inner_array.get(0)
            self.inner_array.remove_at(0)
            return val

    def __str__(self):
        return self.inner_array.__str__()


class Stack:
    def __init__(self):
        self.inner_array = DynamicArray()

    def push(self, val):
        self.inner_array.add(val)

    def pop(self):
        last_element_index = self.inner_array.size() - 1
        val = self.inner_array.get(last_element_index)
        self.inner_array.remove_at(last_element_index)
        return val

    def __str__(self):
        return self.inner_array.__str__()


queue1 = Queue()
queue2 = Queue()
stack = Stack()


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


def menu():
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
                queue1.dequeue()
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
    menu()
stack = []  # this is an empty list
stack.append(10)  # adding on top of the stack
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)  # [10,20,30]

top_element = stack[-1]  # peeking
print("Top element is:", top_element)  # the top element is 30

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")


class SimpleStack:
    def __init__(self):
        self.items = []  # initialize an empty list

    def is_empty(self):
        return len(self.items) ==0

    def push(self, item):
        self.items.append(item)  # adding an item at the top of the stack

    def pop(self):
        if self.is_empty():  #
            raise Exception("Cannot pop an empty stack")  # returns an error if stack is empty
        return self.items.pop()  # removing an item from top and return it

    def peek(self):  # return top item without removing it
        if self.is_empty():
            raise Exception("STACK IS EMPTY")
        return self.items[-1]  # minus 1 returns last item

    def size(self):
        return len(self.items)

    def print_stack(self):
        print("Stack from bottom to top", self.items)  # prints all items in the stack from bottom to top
        return


if __name__ == "main":
    stack1 = SimpleStack()

    stack1.push(1000)  # entered first
    stack1.push(2000)
    stack1.push(3000)  # at the top

    stack1.print_stack()  # print the elements

    print("Top element:", stack1.peek())  # this will be 3000
    print("Popped:", stack1.pop())  # 3000 will be removed
    stack1.priint_stack()  # the remaining[1000,2000]

    print("Is stack empty?", stack1.is_empty())  # false because its not empty

    stack1.pop()  # pop all to make it empty
    stack1.pop()
    print("Is stack empty after popping all", stack1.is_empty())








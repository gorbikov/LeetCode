from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        if len(self.q) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.q)

print("pop")
print(obj.pop())
print(obj.q)


print("top")
print(obj.top())
print(obj.q)


print("isempty")
print(obj.empty())
print(obj.q)

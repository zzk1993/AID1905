class StackError(Exception):
    pass

# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 链式栈操作
class LStack:
    def __init__(self):
        # 标记栈的栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self,val):
        self._top = Node(val,self._top)

    def pop(self):
        if self._top is None:
            raise StackError("Stack is emtpy")
        value = self._top.val.next
        return value

    def top(self):
        if self._top is None:
            raise StackError("Stack is emtpy")
        return self._top.val

if __name__ == "__main__":
    ls = LStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    print(ls.pop())
    print(ls.pop())
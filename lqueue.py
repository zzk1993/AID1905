class QueueError(Exception):
    pass

# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next

# 队列操作
class LQueue:
    def __init__(self):
        # 定义队头和队尾的属性变量
        self.front=self.rear=Node(None)

    def is_empty(self):
        return self.front == self.rear

    # 入队  rear动
    def enqueue(self,val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    # 出队  front动
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")
        self.front = self.front.next
        return self.front.val

if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())

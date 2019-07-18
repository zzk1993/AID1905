class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self._elems=[]

    def is_empty(self):
        return self._elems==[]

    def enqueue(self,val):
        self._elems.append(val)

    def dequeue(self):
        if self.is_empty():
            raise QueueError("kong")
        return self._elems.pop(0)



if __name__ == "__main__":
    sq=SQueue()
    for i in range(50):
        sq.enqueue(i)
    from day02.demo1 import*
    st= SStack()
    while not sq.is_empty():
        st.push(sq.dequeue())
    while not sq.is_empty():
        sq.enqueue(st.pop())
    while not sq.is_empty():
        print(sq.dequeue())



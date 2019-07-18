"""
sstack.py栈模型的顺序存储

思路总结:
1.列表即顺序储存,但功能多,不符合栈的模型特征
2.利用列表将其封装,提供接口方法
"""
#顺序栈类
class StackError(Exception):
    pass


class SStack:
    def __init__(self):
        #列表的最后一个元素作为栈顶
        self._elems=[]#空列表就是栈的存储空间

    def is_empty(self):
        return self._elems==[]

    def push(self, val):
        self._elems.append(val)

    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        # 弹出并返回
        return self._elems.pop()

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems[-1]





if __name__=="__main__":
    st=SStack()

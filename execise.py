from linklist import *
l1=LinkList()
l2=LinkList()

l1.init_list([1,5,20,7,8,56])
l2.init_list([2,3,4,8,46,23,8,64,4])
l1.show()
l2.show()



def merge(l1,l2):
    p=l1.head
    q=l2.head.next
    while p.next is not None:
        if p.next.val<q.val:
            p=p.next
        else:
            tmp=p.next
            p.next=q
            p=p.next
            q=tmp
    p.next=q
merge(l1,l2)
l1.show()
from day02.demo1 import *
st=SStack()
while True:
    exp= input()
    tmp=exp.split(' ')
    for i in tmp:
        if i not in["+","-","*","/"]:
            st.push(int(i))
        elif i=="+":
            x=st.pop()
            y=st.pop()
            st.push(x+y)
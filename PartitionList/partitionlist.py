# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printAll(self,head):
        current = head

        while current is not None:
            print(current.val)
            current = current.next

    def addlast(self, data):
        add = ListNode(data)
        add.data = data

        if self.tail is None:
            self.tail = self.head = add
        else:
            self.tail.next = add
            self.tail = add

class Solution(object):
    def partition(self, head, x):
        temp = head

        hold1 = current1 = ListNode()
        hold2 = current2 = ListNode()

        while temp:
            if temp.val < x:
                current1.next = ListNode(temp.val)
                current1 = current1.next
            
            else:   # temp.val >= x
                current2.next = ListNode(temp.val)
                current2 = current2.next

            temp = temp.next

        current1.next = hold2.next  # point last node of '<' list with first node of '>' list 

        return hold1.next

class Test:
    LL = LinkedList()
    llist = [1, 4, 3, 2, 5, 2]
    x = 3

    for i in llist:
        LL.addlast(i)

    test = Solution()
    
    head = test.partition(LL.head, x)
    LL.printAll(head)

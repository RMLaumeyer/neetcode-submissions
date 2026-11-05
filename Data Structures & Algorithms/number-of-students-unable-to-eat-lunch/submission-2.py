class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        head = ListNode(0)
        cur = head
        tail = None
        count = len(students)

        for i in range(len(students)):
            newnode = ListNode(students[i])
            cur.next = newnode
            cur = cur.next
            if(i+1 == len(students)):
                tail = cur
            
            

        head = head.next
        cur = head

        for i in range(len(sandwiches)):
            refused = 0

            while cur.val != sandwiches[i]:
                if refused == count - 1:
                    return count

                temp2 = cur
                temp = cur.next
                cur = temp
                head = cur

                tail.next = temp2
                tail = tail.next
                tail.next = None

                refused += 1

            temp = cur.next
            cur = temp
            head = cur
            count -= 1

            if count == 0:
                return 0


 
        return count


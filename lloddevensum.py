#  Maximum odd-even sum of a linked list: Given a linkedlist, find the maximum sum sum of pairs of alternate elements.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def maxOddEvenSum(self, head):
        odd_sum = 0
        even_sum = 0
        pos = 1
        curr = head

        while curr:
            if pos % 2 == 1: 
                odd_sum += curr.val
            else:  
                even_sum += curr.val
            curr = curr.next
            pos += 1

        return max(odd_sum, even_sum)

def create_linked_list():
    values = input("Enter the values of the linked list (space-separated): ").split()
    head = ListNode(int(values[0]))
    current = head

    for value in values[1:]:
        current.next = ListNode(int(value))
        current = current.next

    return head
    
head = create_linked_list()
solution = Solution()
result = solution.maxOddEvenSum(head)
print("Maximum Odd-Even Sum of alternate pairs:", result)


# Reverse a linked list: Given a linked list, reverse the linked lst and return the pointer to the reversed list.


class ListNode(object):
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution(object):
  def reverseList(self, head):
      prev = None
      curr = head

      while curr:
          nxt = curr.next
          curr.next = prev
          prev = curr
          curr = nxt

      return prev

def create_linked_list():
  values = input("Enter the values of the linked list (space-separated): ").split()
  head = ListNode(int(values[0]))
  current = head

  for value in values[1:]:
      current.next = ListNode(int(value))
      current = current.next

  return head

def print_linked_list(head):
  current = head
  while current:
      print(current.val, end=" -> " if current.next else "\n")
      current = current.next

head = create_linked_list()
solution = Solution()

print("Original linked list:")
print_linked_list(head)

reversed_head = solution.reverseList(head)

print("Reversed linked list:")
print_linked_list(reversed_head)

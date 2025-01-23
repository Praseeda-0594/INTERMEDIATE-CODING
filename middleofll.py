# Middle of a linked list: Given a singly linked list, find the element at the middle of the linked list.


class ListNode(object):

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution(object):

  def middleNode(self, head):
    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    return slow


def create_linked_list():
  values = input(
      "Enter the values of the linked list (space-separated): ").split()
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

middle = solution.middleNode(head)
print("Middle node of the linked list:", middle.val if middle else "None")

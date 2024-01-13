def reverse(head):
  tail = None
  while head:
    coming = head.next
    head.next = tail
    tail = coming
    head = coming
  return tail

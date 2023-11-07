def hasCycle(self, head):
  # intializing two pointers 
  # slow pointer
  p1 = head
  # fast pointer
  p2 = head

  # checking if the Linked list has an end
  while (p2!=None) and (p2.next!=None):
    p1 = p1.next
    p2 = p2.next.next

    # return True if both pointers coincide
    if p1 == p2:
      return True

  return False

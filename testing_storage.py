dl = CircularList()
print(dl.is_empty(), True)
print(dl.__str__(), '[]')
print(dl.remove_front(), False)
print(dl.remove_back(), False)
dl.add_front(80)
print(dl.is_empty(), False)
print(dl.__str__())
dl.add_front(70)
print(dl.__str__())
dl.add_front(60)
print(dl.__str__())
dl.add_back(90)
print(dl.__str__())
print(dl.get_front(),
      dl.get_back())
print(dl.remove_front(), True)
print(dl.remove_back(), True)
print(dl.__str__())
print(dl.contains(90), False)
print(dl.contains(70), True)
print(dl.remove(80),
      dl.remove(90), 'Hello')
dl.add_front(60)
dl.add_back(80)
dl.add_back(90)
dl.remove_link(3)
dl.remove_link(0)
dl.add_link_before(50, 0)
dl.add_link_before(60, 1)
# dl.add_link_before(100, 40)
print(dl.__str__())
dl.circularListReverse()

print(dl.__str__())

print(dl.__str__())

ml = LinkedList()
print(ml.is_empty())
print(ml.get_back())
print(ml.get_front())
ml.add_back('A')
ml.add_front('Z')
print(ml.__str__())
ml.add_link_before('A', 0)
ml.add_link_before('B', 0)
print(ml.__str__())
ml.add_link_before('C', 1)
print(ml.__str__())
ml.add_link_before(80, 1)
print(ml.__str__())
ml.add_link_before(40, 2)
print(ml.__str__())
# ml.add_link_before(44, -1)
# ml.add_link_before(44, 20)
ml.add_front('A')
ml.add_back('A')
print(ml.__str__())
ml.remove_link(1)
ml.remove_link(0)
print(ml.get_front())
print(ml.get_back())
print(ml.is_empty(), 'false')
print(ml.contains('D'), 'false')
print(ml.contains('C'), 'true')
ml.remove_link(-20)
ml.remove_front()
ml.remove_back()
ml.remove('A')
print(ml.__str__())

while cur.data != None:
      next_cur = cur.next  # stores the next node

      prev.next = prev.prev
      prev.prev = cur
      cur.next = prev  # sets next to point backwards
      cur.prev = next_cur

      # I'm like 73% on why this worked...
      prev = cur
      cur = next_cur


previous = cur.prev
cur.prev = cur.next
cur.next = previous
cur = cur.prev
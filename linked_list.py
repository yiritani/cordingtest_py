class Node:
	def __init__(self, data, next_node = None):
		self.data = data
		self.next = next_node

class Link:
	def __init__(self, data=None):
		self.head = data

	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node


	def insert(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def print(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next

	def reverse(self):
		def _reverse(current, prev):
			if not current:
				return prev
			new_node = current.next
			current.next = prev
			prev = current
			current = new_node
			return _reverse(current, prev)
		self.head = _reverse(self.head, None)

l = Link()
l.append(1)
l.append(2)
l.insert(0)
l.reverse()
l.print()

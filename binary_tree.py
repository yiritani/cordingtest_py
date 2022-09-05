class Node:
	def __init__(self, data):
		self.value = data
		self.left = None
		self.right = None


def insert(node, value):
	if node is None:
		return Node(value)
	if node.value > value:
		node.left = insert(node.left, value)
	if node.value < value:
		node.right = insert(node.right, value)
	return node


def search(node, value):
	if node is None:
		return False
	if node.value == value:
		return True
	if node.value > value:
		return search(node.left, value)
	if node.value < value:
		return search(node.right, value)

	return False

l = None
for i in [3, 6, 2, 7, 5, 1]:
	l = insert(l, i)

print(search(l, 8))

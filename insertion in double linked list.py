def insertAfter(self, next_node, new_data):
	if next_node is None:
		print("This node doesn't exist in DLL")
		return
	new_node = Node(data=new_data)
	else:
		head = new_node


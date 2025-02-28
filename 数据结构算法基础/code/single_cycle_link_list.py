class Node:
	def __init__(self, item):
		self.elem = item
		self.next = None


class SingleCycleLinkList：
	"""单向循环链表"""
	def __init__(self, node=None):
		self.__head = node
		if node:
			node.next=node  # 循环 指向自己
	
	def is_empty(self):
		"""链表是否为空"""
		return self.__head == None

	def length(self):
		"""链表长度"""
		if self.is_empty():
			return 0
		# cur游标，用来移动遍历结点
		cur = self.__head
		# count记录数量
		count = 1
		while cur.next != self.__head:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历整个链表"""
		if self.is_empty():
			return
		cur = self.__head
		while cur.next != self.__head:
			print(cur.elem, end=" ")
			cur = cur.next
		# 退出循环，cur指向尾节点，但尾结点的元素未打印
		print(cur.elem)

	def add(self, item):
		"""链表头部添加元素，头插法"""
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			# 退出循环
			node.next = self.__head
			self.__head = node
			# cur.next = node
			cur.next = self.__head			

	def append(self, item):
		"""链表尾部添加元素，尾插法"""
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			node.next = self.__head
			cur.next = node


	def insert(self, pos, item):
		"""指定位置添加元素
		：params pos 从0开始
		"""
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			pre = self.__head
			count = 0
			while count < (pos-1):
				count += 1
				pre = pre.next
			# 当退出循环后，pre指向pos-1位置
			node = Node(item)
			node.next = pre.next
			pre.next = node

	def remove(self, item):
		"""删除结点"""
		cur = self.__head
		pre = None
		while cur.next != self.__head:
			if cur.elem == item:
				# 先判断此节点是否是头结点
				if cur == self.__head:
					# 头结点的情况
					# 找尾结点
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
					self.__head = cur.next
					rear.next = self.__head
				else:
					# 中间结点
					pre.next = cur.next
				return
			else:
				pre = cur
				cur = cur.next
		# 退出循环，cur指向尾结点
		if cur.elem == item:
			if cur == self.__head:
				# 链表只有一个结点
				self.__head = None
			else:
				pre.next = cur.next

	def search(self, item):
		"""查找结点是否存在"""
		if self.is_empty():
			return False
		cur = self.__head
		while cur.next != self.__head:
			 if cur.elem == item:
			 	return True
			 else:
			 	cur = cur.next
		# 退出循环，cur指向尾结点
		if cur.elem == item:
			return True
		return False		



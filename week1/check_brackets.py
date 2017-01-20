class Stack:

	def __init__(self):
		self.data = []

	def push(self, data):
		self.data.append(data)

	def pop(self):
		return self.data.pop()

	def top(self):
		return self.data[-1]


stack = Stack()

def checker(string):
	for i in range(len(string)):
		if string[i] in  ["[", "(", "{"]:
			stack.push((string[i], i))

		elif string[i] in [")", "]", "}"]:
			if not stack.data:
				return i[1]

			top = stack.pop()
			char = string[i][0]
			if (char=="[" and top=="]") or (char=="{" and top=="}") or (char=="(" and top==")"):
				return i[1]
	if stack.data:
		top = stack.pop()
		return i[1]

	return "Success"

			



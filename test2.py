class Fifo1:
	def __init__(self, max_size=10):
		self.arr = []
		self.max_size = max_size
		self.size = 0
	def put(self, val):
		self.arr.append(val)
	def pop(self):
		if len(self.arr) > 0:
		    return self.arr.pop(0)
		else:
			print("Очередь пуста")
		
class Fifo2:
    def __init__(self, max_size=10):
        self.buffer = [None]*max_size
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_size = max_size
        
    def enqueue(self, item):
        if self.size == self.max_size:
        	print("Очередь заполненна")
        else:
        	self.tail = (self.tail +1) % self.max_size
        	self.size += 1
        	self.buffer[self.tail] = item
    def dequeue(self):
        if self.size == 0:
        	print("Очередь пуста")
        else:
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            item = self.buffer[self.head]
            return item

print("Fifo1")
f = Fifo1()
f.put(1)
f.put(2)
f.put(3)

print(f.pop())
print(f.pop())
print(f.pop())
print(f.pop())

print("Fifo2")
f2 = Fifo2(3)
f2.enqueue(1)
f2.enqueue(2)
f2.enqueue(3)

print(f2.dequeue())
print(f2.dequeue())
print(f2.dequeue())
print(f2.dequeue())

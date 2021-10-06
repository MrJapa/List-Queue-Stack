from time import sleep
class Queue:

	def __init__(self):
		self.elements = []

	def enqueue(self, data):
		self.elements.append(data)
		return data

	def dequeue(self):
		return self.elements.pop(0)

	def rear(self):
		return self.elements[-1]

	def front(self):
		return self.elements[0]

	def is_empty(self):
		return len(self.elements) == 0

if __name__ == '__main__':
    queue = Queue()

print(f"Er køen tom?: {queue.is_empty()}\n")

sleep(2)

print(f"{queue.enqueue(1)}: Er nu i køen")
print(f"{queue.enqueue(2)}: Er nu i køen")
print(f"{queue.enqueue(3)}: Er nu i køen")
print(f"{queue.enqueue(4)}: Er nu i køen")
print(f"{queue.enqueue(5)}: Er nu i køen")
print(f"{queue.enqueue(6)}: Er nu i køen")
print(f"{queue.enqueue(7)}: Er nu i køen")
print(f"{queue.enqueue(8)}: Er nu i køen\n")

sleep(2)

print(f"Første element i køen: {queue.front()}\n")

sleep(2)

print(f"Sidste element i køen: {queue.rear()}\n")

sleep(2)

i = 1
while(i <= 5):
    print(f"{queue.dequeue()}: Er nu ude af køen")
    i += 1

sleep(2)

print(f"\nEr køen tom?: {queue.is_empty()}\n")

sleep(2)

print(f"Først element i køen: {queue.front()}\n")

sleep(2)

while(i <= 8):
    print(f"{queue.dequeue()}: Er nu ude af køen")
    i += 1

sleep(2)

print(f"\nEr køen tom?: {queue.is_empty()}\n")
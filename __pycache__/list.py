class Listen():
    
    def __init__(self) -> None:
        self.array = []
        
    def insert(self,data):
        self.array.append(data)
        return data

    def contains(self):
        return len(self.array) == 0

    def count(self):
        print(f"Antal i listen: {len(self.array)}")

l = Listen()
print(f"Tilføjede {l.insert(1)}")
print(f"Tilføjede {l.insert(2)}")
print(f"Tilføjede {l.insert(3)}")
print(f"Tilføjede {l.insert(4)}")
print(f"Tilføjede {l.insert(5)}")
print(f"Tilføjede {l.insert(6)}")
print(f"Tilføjede {l.insert(7)}")

l.count()

print("\n")

for i in range(len(l.array)):
    print(l.array[i])

l.array.remove(1)
l.array.remove(3)
l.array.remove(5)
l.array.remove(7)

print("\n")

print("Tal i listen efter sletning")
for i in range(len(l.array)):
    print(l.array[i])

print("\n")
l.count()
print("\n")
print(f"Er listen tom?: {l.contains()}\n")

l.array = []

print(f"Ny liste antal: {l.count()}")
print(f"Er listen tom?: {l.contains()}")


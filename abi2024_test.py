from abi2024 import *

dynArray = DynArray()

if dynArray.isEmpty():
    print("DynArray is Empty")

dynArray.append("Hello")
dynArray.append("Test")
dynArray.append("Lol")

print(dynArray.getItem(1))

print(dynArray.getLength())

dynArray.insertAt(1, "Peter")

print(dynArray.getItem(1))

dynArray.delete(1)

dynArray.setItem(1, "Hans")

print(dynArray.getItem(1))

print("DynArray Complete")
print("__________________________________________")

stack = Stack()

stack.push("Hello World")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
stack.push("Karl")
print(stack.pop())
print(stack.top())
if stack.isEmpty():
    print("Stack is Empty")

print("Stack Completed")
print("__________________________________________")

queue = Queue()

queue.enqueue("Hans")
queue.enqueue("Peter")

print(queue.dequeue())
print(queue.head())

if queue.isEmpty():
    print("Queue is Empty")

print("Queue Completed")
print("__________________________________________")

binTree = BinTree("Fedor")

print(binTree.isLeaf())

binTree.setLeft(BinTree("Karl"))

print(binTree.isLeaf())

print(binTree.hasLeft())

print(binTree.getLeft().isLeaf())

binTree.deleteLeft()

print(binTree.isLeaf())

binTree.setRight(BinTree("Marc"))

print(binTree.hasRight())

print(binTree.getRight().isLeaf())





print("BinTree Completed")
print("__________________________________________")
from abi2024 import *

def queuesort(queue: Queue) -> Queue:
    sorted = Queue()
    while not queue.isEmpty():
        highest = queue.dequeue()
        while not sorted.isEmpty() and sorted.head() < highest:
            queue.enqueue(sorted.dequeue())
        sorted.enqueue(highest)
    return sorted

alter = Queue()

alter.enqueue(21)
alter.enqueue(20)
alter.enqueue(33)
alter.enqueue(30)
alter.enqueue(27)
alter.enqueue(28)
alter.enqueue(31)
alter.enqueue(19)

alter = queuesort(alter)

while not alter.isEmpty():
    print(alter.dequeue())

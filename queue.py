#!/usr/bin/python3

#define queue class
class Queue:
    #constructor function
    def __init__(self):
        self._queue = list()

    #insert function
    def insert(self, value):
        self._queue.append(value)

    #remove function
    def remove(self):
        try:
            self._queue[0]
        except:
            print("The queue is empty")
        else:
            print(self._queue.pop(0))

queue = Queue()
queue.insert(5)
queue.insert(6)
val = queue.remove()

print(val)
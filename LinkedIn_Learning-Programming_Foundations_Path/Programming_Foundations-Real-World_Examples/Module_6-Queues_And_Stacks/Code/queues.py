'''
    Queues:
            - They're a data structure that allows you to store and retrieve data in an order system
              called 'FIFO' short for 'First In First Out' so what you put first, will be the first to
              be returned.

            - To use, we should import queue
            
            - clients_queue = queue.Queue()
                This way, it's an infinite large queue, to make a queue of a specific size, pass
                the size you want to the constructor: Queue(25)
            
            - We can check whether a queue is full() or empty()
            
            - We can get() data from a queue:
                - It'll return the first item that's been put and the one after and so on in this order.
                - When the queue gets empty, your program will get stuck because the put() method
                  will be in a "blocking" mode which means, it'll keep waiting to receive an item
                  to store, to overcome thsi problem we can tell the method that if there's no data
                  to be stored break, which would cause it to return an error.
            
            - We also can put() items into a queue, and the same issues that might happen with get()
              can possibly happen with put() and you can overcome them in such a similar way.

'''

from http import client
import queue

customers = queue.Queue()

print()
print('Is customers queue empty? {}'.format(customers.empty()))
print('Is customers queue full? {}'.format(customers.full()))

customers.put('Mohammed')
customers.put('Ahmed')
customers.put('Ali')
customers.put('Khaled')

print()
print('Is customers queue empty? {}'.format(customers.empty()))
print('Is customers queue full? {}'.format(customers.full()))


print(customers.get())
print(customers.get())
print(customers.get())
print(customers.get())

print()
print('Is customers queue empty? {}'.format(customers.empty()))
print('Is customers queue full? {}'.format(customers.full()))


clients = queue.Queue(3)
clients.put('C 1')
clients.put('C 2')
clients.put('C 3')

# this would run infinitely
# clients.put('C 4')

# this would return an error
# clients.put('c 5', False)

print()
print('Is Clients queue empty? {}'.format(clients.empty()))
print('Is Clients queue full? {}'.format(clients.full()))

print(clients.get())
print(clients.get())
print(clients.get())

#This would return an error
print(clients.get(False))

# This would run infinitely
print(clients.get())

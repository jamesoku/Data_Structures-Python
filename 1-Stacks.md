# Stacks
A stack is a type of data structure that uses last-in, first-out ordering to store items. LIFO is a common term used to describe this. In a stack, an element
is only removed from one end while a new element is put to the other end.

![img1](img1.jpg)



## Stack Functions and time complexity

| Function      | Explanation                                       | Time complexity|
| ------------- | ------------------------------------------------- | -------------- |
| empty()       | Returns whether the stack is empty                | O(1)           |
| size()        | Returns the size of the stack                     | O(1)           |
| top() / peek()| Returns a reference to the topmost element of the stack|  O(1)     |
| push()|  Inserts an element at the top of the stack |  O(1)     |
| pop() | Deletes the topmost element of the stack |  O(1)     |

![img2](img2.jpg)

## Implementation

There are different ways from which a stack can be implemented in Python.

* List
* Collections.deque
* queue.LifoQueue

### List Implementation and example
A stack can be created using the built-in list structure, which you probably use frequently in your apps. You can use .append() rather than .push() to add new elements to the top of your stack, and .pop() to remove them in LIFO order.
The main problem is that as it expands, it may experience speed problems. The list's contents are kept in close proximity to one another in memory; if the stack expands beyond the block of memory that can accommodate it, memory allocations must be made by Python. As a result, some add() calls may take significantly longer than others.

List implementation examples:
Bob is trying to add 2 people to the list of people in his soccer team and remove the last person he add using python:

```python
        # Python program to
    # demonstrate pop and append function.

team = ['jack','henry','phil']
print(team)

    # pop() function to pop
    # element from stack in
    # LIFO order. Removing the last two players from the list.
print('\nPlayers popped from team:')
print(team.pop())
print(team.pop())


    # append() function to push
    # element in the stack. Adding two new players to the team.
print('\nPlayers appended to team:')
team.append('messi')
team.append('ronaldo')
print(team)
```

Output
```python
['jack', 'henry', 'phil']

Players popped from team:
phil
henry

Players appended to team:
['jack', 'messi', 'ronaldo']
```


### Collections.deque Implementation

Utilizing the deque class from the collections module, a Python stack may be created. When we need faster append and pop operations from both ends of the container, deque is favored over lists because deque offers an O(1) time complexity for append and pop operations, whereas lists offer an O(n) time complexity.


```python
    # Python program to
    # demonstrate stack implementation
    # using collections.deque

    from collections import deque

    team = deque()
    print(team)

    # append() function to push
    # element in the stack. Adding two new players to the team.
    print('\nPlayers appended to team:')
    team.append('messi')
    team.append('ronaldo')
    print('Initial stack:')
    print(team)

    # pop() function to pop
    # element from stack in
    # LIFO order. Removing the last two players from the list.
    print('\nPlayers popped from team:')
    print(team.pop())
    print(team.pop())
    print(team)

```

Output
```python
deque([])

Players appended to team:  
Initial stack:
deque(['messi', 'ronaldo'])

Players popped from team:  
ronaldo
messi
deque([])
```


### queue.LifoQueue Implementation
How do you create a Python stack for a threaded program since you can't use list for a stack if you're threading and you probably don't want to use deque for a stack?
The queue module, queue, contains the solution.
LifoQueue. Do you recall how you discovered that the Last-In/First-Out rule governs stacks? That's what the "Lifo" in LifoQueue stands for, after all.
LifoQueue uses .put() and .get() to add and remove data from the stack, but the interface for list and deque was similar.

There are various functions available in this module: 

* maxsize – Number of items allowed in the queue.
* empty() – Return True if the queue is empty, False otherwise.
* full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
* get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
* get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
* put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
* put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
* qsize() – Return the number of items in the queue.

```python
# Python program to
# demonstrate stack implementation
# using collections.deque

from queue import LifoQueue

team = LifoQueue(maxsize=3)
print(team)

# qsize() show the number of elements
# in the stack
print(team.qsize())

# put() function to push
# element in the stack
print('\nPlayers appended to team:')

team.put('messi')
team.put('ronaldo')
team.put('neymar')
    
print("Full: ", stack.full())
print("Size: ", stack.qsize())

# pop() function to pop
# element from stack in
# LIFO order. Removing the last two players from the list.
# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(team.get())
print(team.get())
print(team.get())
 
print("\nEmpty: ", stack.empty())

```

Output
```python
<queue.LifoQueue object at 0x0000018ED0D51E20>
0

Players appended to team:
Full:  True
Size:  3

Elements popped from the stack
neymar
ronaldo
messi

Empty:  True
```

### Conlclusion
In general, if you're not using threading, you should use a deque. Unless you've analyzed your performance and determined that a slight increase in pushing and popping speed will make a significant enough impact to justify the maintenance risks, you should utilize a LifoQueue if you're using threading.

list might be common, but it should be avoided because it might have problems with memory reallocation. The best option for your non-threaded Python stack is deque because their APIs are the same and deque doesn't have these problems.

### Coding Problem
 
Print the Next Greater Element (NGE) for each element in an array. The first greater element in the array on the right side of an element x is considered to be its next greater element. When there is no greater element for an element, the next greater element is treated as -1.


Example:

- The next bigger element in an array is always represented as -1 in the rightmost element.

- Every element in a decreasingly sorted array has -1 as the next greater element.

- The subsequent bigger items for each element in the input array [4, 5, 2, 25] are as follows.

```
Element       NGE
   4      -->   5
   5      -->   25
   2      -->   25
   25     -->   -1
```
- For the input array [13, 7, 6, 12}, the next greater elements for each element are as follows. 

```
Element        NGE
   13      -->    -1
   7       -->     12
   6       -->     12
   12      -->     -1
```
You can check your code with the solution here: [Solution](stack_solution.py)

[Back to Welcome Page](outline.md)
# Sets
A Set is an iterable, changeable, and duplicate-free unordered collection data type. The mathematical concept of a set is represented by the set class in Python. A set has a highly optimized way for determining whether a certain element is contained in the set, which is its main advantage over a list. This is based on a hash table, a type of data structure. Since sets are not ordered, we cannot use indexes to access items like we do with lists.

The built-in set type in Python includes the following features:

* Sets have no order.
* Set components are special. Elements cannot have duplicates.
* Although the elements that make up a set may be changed, the set itself must be immutable.


## Hashing
Hashing is a technique or process of mapping keys, and values into the hash table by using a hash function. It is done for faster access to elements. The efficiency of mapping depends on the efficiency of the hash function used.

![hash](hashtable.png)
## Sets methods and time complexity

| Function      | Explanation                                       | Time complexity|
| ------------- | ------------------------------------------------- | -------------- |
| add()       | Adds an element to the set   | O(1)           |
| clear()        | Removes all the elements from the set | O(1)|
| copy()     | Returns a copy of the set | O(n)|
| intersection() | Returns a set, that is the intersection of two other sets |  O(n)     |
| pop() | Removes an element from the set |  O(1)     |
| remove() | Removes the specified element |  O(1)     |
| union() | Return a set containing the union of sets |  O(n)     |


## Implementation
### Frozen Sets

Python supports only methods and operators that deliver results without changing the frozen set or sets to which they are applied. Frozen sets are immutable objects. A set's components can be changed at any moment, but the components of a frozen set don't change after they've been created.
It returns an empty frozenset if no arguments are supplied.

```python
    # The python file below cannot compile because the user is trying to change an item in a set
    
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
x[1] = "strawberry" #Trying to change an item in a set
print(x)
```

Output:
```python
Traceback (most recent call last):
  File "demo_ref_frozenset2.py", line 3, in <module>
    x[1] = "strawberry"
TypeError: 'frozenset' object does not support item assignment
```
### Creating Python Sets
All of the components (items) must be enclosed in curly braces {}, separated by commas, or can be formed as a set by using the set() function.

There may be any number of things and various sorts inside it (integer, float, tuple, string etc.). However, a set cannot contain mutable items, such as lists, sets, or dictionaries.

```python
# Initializing a set
my_set = {}
print(my_set)

my_set = set()
print(my_set)

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
```

Output
```python
{}
set()
{1, 2, 3}
{'Hello', 1.0, (1, 2, 3)}
```

### Modifying a set in Python
Sets can be changed. However, indexing is useless because they are unordered.

Indexing or slicing cannot be used to access or modify a set element. It is not supported by the set data type.

The add() method can be used to add a single element, and the update() method can be used to add many components. Tuples, lists, strings, and other sets can be passed to the update() method as arguments. Duplicates are avoided at all costs.

```python
# initialize my_set
my_set = {1, 3}
print(my_set)

# my_set[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not support indexing

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)

```

```python
{1, 3}
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4, 5, 6, 8}
```
### Removing elements from a set
A particular item can be removed from a set using the methods discard() and remove().

The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set. On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).

```python
# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

my_set.remove(2)
```
Output
```python
{1, 3, 4, 5, 6}
{1, 3, 5, 6}
{1, 3, 5}
{1, 3, 5}
Traceback (most recent call last):
  File "<string>", line 28, in <module>
KeyError: 2
```
The pop() method can be used in a similar way to delete and return an object.

Set is an unordered data type, hence it is impossible to predict which item will be displayed. It is entirely random.

The clear() method can also be used to eliminate every item from a set.

```python
# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)
```
Output
```python
{'H', 'l', 'r', 'W', 'o', 'd', 'e'}
H
{'r', 'W', 'o', 'd', 'e'}
set()
```
### Python Set Operations
Mathematical set operations like union, intersection, difference, and symmetric difference can be performed on sets. With operators or methods, we can accomplish this.

![](set-pic.png)

Union of A and B is a set of all elements from both sets.

Union is performed using | operator. Same can be accomplished using the union() method.
![](set.png)

```python
# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

# use union function
print(A.union(B))
```

Output
```python
{1, 2, 3, 4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8}
```

### Set Intersection
Intersection of A and B is a set of elements that are common in both the sets.

Intersection is performed using & operator. Same can be accomplished using the intersection() method.

```python
# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)

# use intersection function on A
print(A.intersection(B))
```

Output
```python
{4, 5}
{4, 5}
```

### Set Difference
A set of components that are exclusively in A but not in B make up the difference between the sets A and B (A - B). A group of items in B but not in A is known as B-A.

The - operator is used to perform a difference. The difference() method can do the same.

```python
# Difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)

# use difference function on A
print(A.difference(B))
```
Output
```python
{1, 2, 3}
{1, 2, 3}
```

### Conclusion
In this tutorial, you learned how to define set objects in Python, and you became familiar with the functions, operators, and methods that can be used to work with sets.

You should now be comfortable with the basic built-in data types that Python provides.

### Coding Problem
Your goal is to write a program that will find and display all pairs of numbers in a list that sum up to 10. No duplicates should be displayed. This could be done in O(n^2) with a loop within a loop. However, using a set, this can be done in O(n) time. You should assume that the list of numbers provided has no duplicates.

```python
def display_sums(numbers):
    """
    Display pairs of numbers (no duplicates should be displayed) that sum to 
    10 using a set in O(n) time.  We are assuming that there are no duplicates 
    in the list.
    """
    pass

display_sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
"""
Should show something like (order does not matter):
6 4
7 3
8 2
9 1 
"""
print("===========")
display_sums([-20, -15, -10, -5, 0, 5, 10, 15, 20]) 
"""
Should show something like (order does not matter):
10 0
15 -5
20 -10
"""
print("===========")
display_sums([5, 11, 2, -4, 6, 8, -1])
"""
Should show something like (order does not matter):
8 2
-1 11
"""
```
- You can check your code with the solution here: [Solution](set_solution.py)

[Back to Welcome Page](0-Welcome.md)
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
    
print("Full: ", team.full())
print("Size: ", team.qsize())

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
 
print("\nEmpty: ", team.empty())
#importing the collections module with Chainmap
from collections import deque


#input as iterable:
l = 'wow'


""" ------------------------------------------------------------------------------------
                                using deque class
    ------------------------------------------------------------------------------------ """

#creating deque
dq = deque(l) #-> deque(['w', 'o', 'w'])



""" ------------------------------------------------------------------------------------
                                atributes and methods
    ------------------------------------------------------------------------------------ """

#Deque.append(x) -> adds x to the tail
dq.append('j') #-> deque(['w', 'o', 'w', 'j'])


#Deque.appendleft(x) -> adds x to the head
dq.appendleft('l') #-> deque(['l', w', 'o', 'w', 'j'])


#Deque.extend(iterable) -> Adds the iterable elements to the end of the deque
dq.extend('jkl') #-> deque(['l', 'w', 'o', 'w', 'j', 'j', 'k', 'l'])


#Deque.extendleft(iterable) -> Adds the iterable elements to the end of the deque in reverse order
dq.extend('jkl') #-> deque(['l', 'k', 'j', l', 'w', 'o', 'w', 'j', 'j', 'k', 'l'])


#Deque.insert(i, x) -> adds x to given i position
dq.insert(2, 'w')

#Deque.clear() -> deletes all the iterms
dq.clear() #-> deque([])


#Deque.copy() -> copies the deque
cp = dq.copy()


#add some values to continue working
dq.extend('lol') #-> deque(['l', 'o', 'l'])

#Deque.count(x) -> counts the x
dq.count('l') #-> 2


#Deque.index(x, start, stop) -> searches the x's index from start index to stop index
dq.index('l', 1) #-> 2


#Deque.pop() -> deletes and prints last item
dq.pop()


#Deque.popleft() -> deletes head item and prints it
dq.popleft()


#deque to list
print(list(dq)) #-> ['l', 'o', 'l']

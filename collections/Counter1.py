#importing the collections module with Chainmap
from collections import Counter

""" syntax:
    cnt = collections.Counter(iterable or mapping) """

#this class counts how many items


""" ------------------------------------------------------------------------------------
                                using Counter class
    ------------------------------------------------------------------------------------ """

#Creating dict
cnt = Counter('jlj') #-> Counter({'j': 2, 'l': 1})


#other way
cnt = Counter(cats=3, fox=5) #-> Counter({'fox': 5, 'cats': 3})


#Note: we can do operations that available on dicts


""" ------------------------------------------------------------------------------------
                                atributes and methods
    ------------------------------------------------------------------------------------ """


#Counter.elements() -> value produces the key as many times as possible
cnt = Counter(cats=3, fox=5)
list(cnt.elements())
#output: ['cats', 'cats', 'cats', 'fox', 'fox', 'fox', 'fox', 'fox']

sorted(cnt.elements()) #-> ['cats', 'cats', 'cats', 'fox', 'fox', 'fox', 'fox', 'fox']



#Counter.most_common(n) -> returns the n most repeated elements
Counter('ababc').most_common() #-> [('a', 2), ('b', 2), ('c', 1)]



#Counter.subtract(iterable) -> subtract converst the iterable to Counter and subtracts Counter with new Cunter -> Counter1 - Counter2
it = 'skl'
cnt = Counter('jlk')

print(cnt.subtract(it)) # it prints None, because subtract subtrating the it from cnt

print(cnt) #-> and this is correct, output: Counter({'j': 1, 'l': 0, 'k': 0, 's': -1})



#Counter.total() -> calculates sum of values
cnt = Counter(dogs=2, fox=10) #-> 12


#Counter.update(iterable) -> adds iterable to Counter, and this method is against of subtract
it = 'skl'
cnt = Counter('jlk')
cnt.update(it)

print(cnt)
#output: Counter({'l': 2, 'k': 2, 'j': 1, 's': 1})


""" ------------------------------------------------------------------------------------
                                some operations through Counter
    ------------------------------------------------------------------------------------ """

cnt1 = Counter('jkl')
cnt2 = Counter('sjkl')

(cnt1 - cnt2) #-> subtracts

(cnt1 + cnt2) #-> adds Counter

(cnt1 & cnt2) #-> for the moment idk

(cnt1 | cnt2) #-> idk

list(cnt1)
set(cnt1)
dict(cnt1)

#and so on
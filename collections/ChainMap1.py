#importing the collections module with Chainmap
from collections import ChainMap


#input dicts:
f = {'1' : 1, '2' : 2, '3' : 3, '4' : 4} #f -> first
l = {'5' : 5, '6' : 6}  #l -> last


""" ------------------------------------------------------------------------------------
                                using chainmap class
    ------------------------------------------------------------------------------------ """

d = ChainMap(f, l)
#output: ChainMap({'1': 1, '2': 2, '3': 3, '4': 4}, {'5': 5, '6': 6})

#Note: we can use dict functions on this class


d['1'] = 1 #it deletes 1


del d['5'] #error, bec '5' not in first dict. editing dicts will happen only on first dict, not second or anothers


d.popitem() #deletes first dict's last (key, pair)


d['1'] #call the 1 pair value


#for working with other dicts we have 2 ways, using maps and single editing
del l['5'] #ChainMap({'1': 1, '2': 2, '3': 3}, {'6': 6}), but it changes the original l dict out of chainmap, and the chainmap dict. if we need the original l, we don't may find


#maps
d.maps 
#output: [{'1': 1, '2': 2, '3': 3}, {'6': 6}], not  ChainMap({'1': 1, '2': 2, '3': 3}, {'6': 6})


#reversing
d.maps.reverse()
print(d)
#output: ChainMap({'6': 6}, {'1': 1, '2': 2, '3': 3})


#working with other dicts except first dict
print(d.maps[0]) #-> calls the 0 index dict, {'6': 6}

print(d.maps[1]) #-> calls the 1 index dict, {'1': 1, '2': 2, '3': 3, '4': 4}


#for deleting 
del d.maps[1]['1'] #-> ChainMap({'6': 6}, {'2': 2, '3': 3, '4': 4})

#original dict
print(f)  #-> {'2': 2, '3': 3, '4': 4}, same with chainmap, so if we change chainmap the original dict will change automatically too


#final
print(list(d)) # only prints the keys
#output: ['2', '3', '4', '6']
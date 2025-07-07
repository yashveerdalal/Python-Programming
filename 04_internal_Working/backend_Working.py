# in python every memory allocation has a reference count
# when the reference count reaches zero, the memory is freed
# this is called garbage collection

# there is no datatype for variables in python

# python does not collect garbage immediately for numbers & strings

a = 5
b = 2
a = a + 2
print(a)  

myListOne = [1, 2, 3]
myListTwo = myListOne
myListOne = 'yash'
print(myListOne)
print(myListTwo)

myListOne = [1, 2, 33]
print(myListTwo)
print(myListOne)


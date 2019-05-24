#! python3 
import copy
spam = [1, 2, 3]
print(spam)

spam = [1,'a',3.14]
print(spam)

print(spam[0],spam[-1])

spam = [[1,2],['a','b']]
print(spam[0][1],spam[1][1])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[:-1])

print(len(spam))

spam[-1] = 'dog'
print(spam)

print([1, 3, 4]+['a', 'b', 'c'])

print([2] * 4)

del spam[1]
del spam[-1]
print(spam)

for i in spam:
    print(i,end=' ')

for i in range(len(spam)):
    print(spam[i],end='-')

print('cat' in spam)

print('monkey' in spam)

print('rat' not in spam)

a,b,c = [1,2,3]
print(a,b,c)

a,b,c = c,b,a
print(a,b,c)

spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

spam.append('moose')

spam.insert(1,'chicken')

print(spam)

spam.remove('hi')

spam = [2, 5, 3.14, 1, -7]
print(spam.sort())

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

#sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings. This means uppercase letters come before lowercase letters.

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)

#tuple
eggs = ('hello',32,0.7)
print(eggs)

print(eggs[1:3])

print(len(eggs))

print(type(('a',)))

print(type(('b')))

print(tuple([1,3,3]))

print(list(('a','b','c')))

print(list('hello'))

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
print(cheese)

cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

a = [[1,2,3,[1,23]],[4,5],6]
b = copy.copy(a)
#print(b)
#b = copy.deepcopy(a)
print(b)
print(b[0][3])




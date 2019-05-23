#! python3
import random

def hello():
    print('Hello world!')

hello()

def helloSomebody(name):
    print('hello '+name)

helloSomebody('python')

def getRandomInt():
    return random.randint(1,2)

print(getRandomInt())

spam = print('aa')

print(None == spam)

print('hello',end='')
print('world')

print('a','b','c')

print('a','b','c',sep='-')

# the global statement

def spam3():
    global eggs
    eggs = 'my eggs'

eggs = 'global egg'
spam3()
print(eggs)

def test(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(test(2))
print(test(12))
print(test(0))
print(test(2))

def spam2(divideBy):
    return 42 / divideBy

try:
    print(spam2(2))
    print(spam2(12))
    print(spam2(0))
    print(spam2(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
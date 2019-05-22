#! python3

# and
print(True and True)

print(True and False)

print(False and True)

print(False and False)

# or
print(True or True)

print(True or False)

print(False or True)

print(False or False)

# The Not Operator
print(not True)

print(not False)

# if else statements
name = 'Java'
if name == 'Python':
    print('Hi,'+name)
elif name == 'Java':
    print('你好,'+name)
else:
    print('hello,stranger.')

#while loop statements
spam = 0
while spam < 5:
    #print('Hello,world.')
    spam = spam + 1

# break statements
spam = 0
while spam < 5:
    if spam == 0:
        spam = spam + 1
        continue
    print('Hello,world--.')
    spam = spam + 1
    if spam == 2:
        break

#for Loops and the range() Function
for i in range(3):
    print(i)
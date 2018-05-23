import os

read = open('test.txt');
for each_line in read.readlines():
	(num, char) = each_line.split(':',1);
	print(num,end='');
	print(char,end='');
read.close();

print();

read = open('test.txt');
for each_line in read.readlines():
	try:
		(num, char) = each_line.split(':');
		print(num,end='');
		print(char,end='');
	except:
		print('have a error')
read.close();

print(os.path.exists('test.txt'))

print(os.curdir)

print(os.pardir)

print(os.sep)

print(os.devnull)
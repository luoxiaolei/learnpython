# list
mylist = ["luoxiaolei","baotou"]
print(mylist)

mylist = ["luoxiaolei","baotou",["reading","running"]]
print(mylist)

def print_list(mylist):
	for each_item in mylist:
		print(each_item)

print_list(mylist)

def print_list_recursive(mylist):
	for each_item in mylist:
		if isinstance(each_item,list):
			print_list_recursive(each_item)
		else:
			print(each_item)

print_list_recursive(mylist)
list = ['a','b','c']

#获取列表长度
len(list) 
#新增元素
list.append('e') 
#删除末尾元素
list.pop()
#修改元素
list[1] = 'f'
#获取列表最后一个元素
list[-1]

tuple = ('q','w','e')

dict = {'a' : 1, 'b' : 2}
dict['a'] # 1

dict['a'] = 2
dict['a'] # 2
'c' in dict # False

dict.get('a',defaultValue) # 1
dict.get('d',-1) # -1

dict.pop('b') # 2
dict #{'a' : 1}

s = set([1,3,4])
s.add(5)

s.remove(3)

s1 = set([1,2,3])
s2 = set([2,3,4])
s1 & s2 # {2,3}
s1 | s2 # {1,2,3,4}


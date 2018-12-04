# 数字 py支持三种类型数字 ; 整形 ,浮点型 ,复数  数字是不可变类型
num1 = 10
print(num1)
# 删除变量
del num1

# 数字类型转换
num2 = 20
num3 = float(num2)
print(num2)

# 数字函数
num4 = -20
print(abs(num4))

# 字符串
print('--------------------')
str1 = 'abcd'
print(str1[1])
print(r'\n')
print(str1[1:])

# 列表
print('------------------')
list1 = ['aa', 'bb', 'cc', 'dd']
print(list1[2])
del (list1[1])
print(list1)
for x in list1:
    print(x, end='jjj')

# 元组 元组不能修改
print('---------------')
tup1 = ('aa', 24, 'cc',)
tup2 = ()
# 元组只有一个元素时,需在元素后面加,
tup3 = (12)
print(type(tup3))
tup4 = (12,)
print(type(tup4))
# 元组不能修改,但是可以对元组进行连接,删除,截取
print(tup1 + tup4)

# 字典 可变容器 可存储任意值
print('-------------------')
d = {12: 'val1', 'key2': 'val2'}
print(d[12])
d['key3'] = 'val3'
print(d)
d['key1'] = 'aa'
print(d)
# 删除字典,删除后不存在
# del d
# 清空 清楚字典中的值
d.clear()
print(d)
# 键必须唯一,如果重复,则会被后面覆盖  ,键必须为不可变类型 例如数组,字符串,元组

# 集合 set ,无序的不重复的元素序列,使用set()或{}创建,空集合必须用set(),
print('----------------------------')
parame = {'val1', 'val2', 'val3'}
parame1 = set('val1')
print(parame)
print(parame1)

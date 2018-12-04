#  单行注释

'''这是一个
多行注释'''

# 变量定义 变量不需要声明 没有类型
score = 100

# 输入输出
# high = input("请输入你的升高 : ")
# 字符串拼接
# print("身高为 : "+high)
# print("身高 : %s"%high)

# if判断
print("------------------------")
age = 15
if age > 10:
    print("age > 10")
    print(11)
    if age > 12:
        print("age > 12")

# 变量类型 数字 字符串 列表 元祖 集合 字典
# 数字包含 整数 浮点型 复数 布尔
print("----------------------")
num = 100
print(type(num))
print(isinstance(num, int))

# python3 中 True 和 Flase 定义为关键字,值为 1 和 0 ,可以与数字相加
print('----------------------')
flag = True
print(flag)
print(flag + 1)

# 数值运算
print("---------------------")
a = 30
b = 20
print(a + b)
print(a - b)
print(a * b)
# 除  得到浮点数
print(a / b)
# 除  得到整数
print(a // b)
# 取余
print(a % b)
# 乘方
print(a ** 2)

# 列表 元素可以改变
print('------------------')
list = [100, 'aa', 'bb', 14.2]
print(list)
print(list[1])
# 包含左边,不包含右边
print(list[1:3])
print(list[2:])
# 输出两次
print(list * 2)

# 元组 与列表类似,不能改变
print('------------------')
aa = (100, '154', 200, 1.5)
print(aa)

# 集合
print('------------------')
student = {'tom', 'jim', 'jack'}
print(student)

a = set('avsdfsfs')
b = set('sfaefsdweweaf')
# 差集
print(a - b)
# 并集
print(a | b)
# 交集
print(a & b)
# a 和 b 中不同时存在
print(a ^ b)

# 字典
print('---------------------')
dict = {}
dict['one'] = '1111'
dict[2] = '2222'

tinydict = {'name': 'tom', 'age': 12}

print(dict)
print(dict[2])
print(tinydict['name'])
print(tinydict.keys())
print(tinydict.values())

# 标识符 数字,字母,下划线组成,不能以数字开头
# 关键字
print('--------------------------')
import keyword

print(keyword.kwlist)

# 运算符 算术运算符 比较运算符 赋值运算符 逻辑运算符 位运算符 成员运算符 身份运算符
# 逻辑运算符 and or not
print('-----------------------')
a = True
b = False
print(a and b)
print(a or b)
print(not a)
# 身份运算符 is     is not

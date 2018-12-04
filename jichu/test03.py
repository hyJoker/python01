# if
num = 30
if num < 10:
    print('<10')
elif num >= 10 and num < 20:
    print('>=10 && <20')
else:
    print('>=20')

# 循环 包含 while 和 for 循环
print('-------------------')
sum = 0
i = 1
while i < 3:
    sum += i
    i += 1
print(sum)

count = 0
while count < 3:
    print(count, '小于3')
    count += 1
else:
    print(count)

# for 循环,可以遍历任何序列的项目
str = 'aaabbbccc'
for x in str:
    print(x)

# 遍历数字序列
for x in range(0, 10, 2):
    print(x)

# break 跳出循环,不执行else ,continue跳过本次循环,继续下次循环 ,pass空占位符,不做操作

# 迭代器 iter() next()
print('-------------------------')
list = [1, 2, 3, 4]
it = iter(list)
# print(next(it))
# 迭代器可以用for循环遍历
for x in it:
    print(x)

# 生成器 yield
import sys


def fi(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


# f = fi(10)
# while True:
#     try:
#         print(next(f), end=', ')
#     except StopIteration:
#         sys.exit()

# 函数 不可变对象传值,可变对象传引用

# lambda表达式
print('-----------------------')
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1, 2))

# 模块
import sys
print('--------------')
print("命令行参数如下:")
for i in sys.argv:
    print(i)
print('\n python路径:',sys.path)

#
print('-------------------')
import support
support.print_func("Runoob")

print(dir(support))
# from ...import ...

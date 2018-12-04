# 输入和输出
s = '164'
print(str(1 / 7))
print(repr(1 / 7))

# 读取键盘输入
# str = input('请输入 :')
# print('你输入的值是 : ',str)

# 读和写文件 open(filename,mode)
# f = open('./tmp/foo.txt','w')
# f.write("你好啊111")
# f.close()

f = open('./tmp/foo.txt', 'r')
# str = f.read()
# print(str)
str = f.readlines()
for i in str:
    print(i, end='')
f.close()

#
print('---------------------------')
import MyClass

x = MyClass.MyClass('zhangsan', 15)
print(x.name, '-----', x.age)
print(x.sex)

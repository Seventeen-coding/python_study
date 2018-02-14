age = 20
name = 'Swaroop'

print('{0} was {1} years old when he  wrote this bool'.format(name,age))
print('Why is {0} playing with that python?'.format(name))


print(name  +  ' is ' + str(age) + ' years old')

print('{} was {} years old when he  wrote this bool'.format(name,age))
print('Why is {} playing with that python?'.format(name))

# 对于浮点数 ‘0.333’ 保留小数点后三位
print('{0:3f}'.format(1.0/3))

#使用下划线填充文本，并保持文本字处中间位置
# 使用（^)定义 ‘___hello___’ 字串长度为11
print('{0:_^11}'.format('hello'))
print('{0:#^11}'.format('hello'))

# 基于关键字输出‘Swaroop wrote A Byte of Python’
print('{name} wrote {book}'.format(name = 'Swaroop',book = 'A Byte of python'))

#连续打印不换行
print('a' , end = '')
print('b' , end = '')

#最后以空格键结尾
print('c' , end = ' ')
print('d' , end = ' ')
print('e' , end = ' ')
print('f' , end = ' ')

i = 5
print(i)

# \ 用法
i = i \
    + 1
print(i)

# ''' 多行字串
s = '''This is a multi-line stinrg.
this is the 2nd line.
this is the 3th line.'''
print(s)

length = 5
breadth = 2
area = length * breadth

print('area is ', area)
print('Perimeter is ', 2 * (length + breadth))
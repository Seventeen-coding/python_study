#列表、元组和字符串可以看作序列（Sequence）的某种表现形式
shoplist = ['apple','mango','carrot','banana']

name = 'swaroop'

print('Item 0 is ',shoplist[0])
print('Item 1 is ',shoplist[1])
print('Item 2 is ',shoplist[2])
print('Item 3 is ',shoplist[3])
print('Item -1 is ',shoplist[-1])
print('Item -2 is ',shoplist[-2])

print('Character 0 is', name[0])

print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is',shoplist[:])

# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

#步长 ==》 步伐长度 Step
print('shoplist[::1]',shoplist[::1])
print('shoplist[::1]',shoplist[::2])
print('shoplist[::1]',shoplist[::3])
print('shoplist[::1]',shoplist[::-1])
print('shoplist[::1]',shoplist[::-2])
print('shoplist[::1]',shoplist[::-3])

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

#引用赋值
mylist = shoplist

del shoplist[0]

print('shoplist is ',shoplist)
print('mylist is', mylist)


print('Copy by making a full slice')

#重新生成对象
mylist = shoplist[:]

del mylist[0]

print('shoplist is ', shoplist)
print('mylist is',mylist)
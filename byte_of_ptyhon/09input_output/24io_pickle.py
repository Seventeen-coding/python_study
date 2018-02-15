#encoding=UTF-8

import  pickle
shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile,'wb')

#把shoplist 对象写进文件中
pickle.dump(shoplist,f)

f.close()

del shoplist

f = open(shoplistfile,'rb')

#读取文件中对象
storedlist = pickle.load(f)
print(storedlist)


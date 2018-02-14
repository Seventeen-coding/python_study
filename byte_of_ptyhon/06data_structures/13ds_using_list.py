
#this is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have',len(shoplist),'item to purchase.')

print('These item are', end= ' ')

for item in shoplist:
    print(item, end = ' ')

print('\n')

print('I also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('my shopping list is now',shoplist)

print('The first item I will buy is', shoplist[0])
olditem =shoplist[0]

del  shoplist[0]

print('I bought the ', olditem)
print('my shopping list is now',shoplist)
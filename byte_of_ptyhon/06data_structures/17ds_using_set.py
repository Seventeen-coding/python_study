
#集合（set）是简单对象的无序集合（Collection）

bri = set(['brazil','russia','india'])

if 'india' in bri:
    print('india in bri')
else:
    print('india in bri')

if 'usa' in bri:
    print('usa in bri')
else:
    print('usa not in bri')

bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
bri.remove('russia')
print("bri & bric",bri & bric)
print("bri | bric",bri | bric)


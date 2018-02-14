
def print_max(x,y):
    '''Print this maximum of two numbers.这两个数应该是整数

    The two value must be integers. 打印两个数值中最大数 '''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum' )
    else:
        print(y, 'is maximum' )



print_max(3,5)
print(print_max.__doc__)

def say_hello():
    print('Hello')

say_hello()

def print_max(a,b):
    if (a > b):
        print(a, 'is maximum')
    elif (a == b):
        print(a , 'is equal to', b)
    elif a < b :
        print(b, 'is maximum')
    else:
        print('error')

print_max(4,4)
print_max(3,4)
print_max(4,3)
x = 5
y = 7

print_max(x,y)

x = 'aaa'
y = 'bb'

print_max(x,y)

def func(x):
        print('x is',x)
        x = 2
        print('Changed local x to ', x)

func(x)
print('x is still',x)


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed local x to ', x)


func()
print('x is still', x)

def func_2(message, time = 1):
    print(message*time)

func_2('hello')
func_2('hello' , 5)

def total(a = 5 , *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))


def maximum(x,y):
    if x > y:
         return x
    elif x == y:
        return  'The numbers are equal'
    else:
        return y

print(maximum(2 , 3))
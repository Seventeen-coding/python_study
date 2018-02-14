
#通过命令行输入参数
import sys

print('The command line arguments are :')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is ', sys.path,'\n')
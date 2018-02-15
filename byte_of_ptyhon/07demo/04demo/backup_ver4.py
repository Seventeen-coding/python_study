#使用内置压缩库 zipfile source code : Lib/zipfile.py

import os
import time
import zipfile

root_dir = '.'
# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
# 例如在 Windows 下：
# source = ['"C:\\My Documents"', 'C:\\Code']
# 又例如在 Mac OS X 与 Linux 下：
#source = ['/Users/swa/notes']
# 在这里要注意到我们必须在字符串中使用双引号
# 用以括起其中包含空格的名称。
source = root_dir + os.sep + 'note'

#2. 备份文件必须存储在一个
#主备份目录中
#例如在 Windows 下：
# target_dir = 'E:\\Backup'
# 又例如在 Mac OS X 和 Linux 下：

target_dir = root_dir + os.sep + 'backup'
# 要记得将这里的目录地址修改至你将使用的路径

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录

# 3. 备份文件将打包压缩成 zip 文件。
# 4. zip 压缩文件的文件名由当前日期与时间构成。
today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

#给注释
comment = input('Enter a comment -->')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + \
             '_' + comment.replace(' ','_') + '.zip'


# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

#debug
print('source:',source)
print('target:',target)

# 5. 我们使用 zip 命令将文件打包成 zip 格式
#创建一个zip文件对象，压缩是需要把mode改为‘w’，这个是源码中的注释Open the ZIP file with mode read "r", write "w" or append "a"，a为追加压缩，不会清空原来的zip
with zipfile.ZipFile(target, mode='w') as zipf:
    # 将文件写入zip文件中，即将文件压缩
    zipf.write(source)


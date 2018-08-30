'''
Created on 2018年8月7日

@author: Administrator
'''

"""
文件读写
"""

# try:
#     f = open(r"C:\softs\space\pythoning\src\io_stu\t.txt", 'r')
#     print(f.read())
# except IOError:
#     print("error")
# finally:
#     if f:
#         f.close()


with open(r"C:\softs\space\pythoning\src\io_stu\t.txt", 'r', encoding='utf-8') as f:
#     print(f.read())
    for line in f.readlines():
        print(line.strip())
#  要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件

with open('\\tt.txt', 'w') as f:
    f.write('123测试')




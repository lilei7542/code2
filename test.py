from CaculateWithList import CaculateWithList
a = [1,2,31,61,9]
b = [2,31,4,5,61,71]

result = CaculateWithList.list_a_and_b(a,b)

result.sort()

result2 = (a+b)
print(result2)

#
# if [ -f "D:\code\code\code2\message_ass.db.03.txt" ];then
#     echo "文件存在"
# else
#     echo "文件不存在"
#


import os

if (os.path.exists('message_ass.db.03.txt')):
    print(1)
else:
    print(2)


from configparser import ConfigParser
parser = ConfigParser()
parser.read('config.ini',encoding='utf-8')
filepath_ori = parser.get('file','filepath_ori')

print(filename)
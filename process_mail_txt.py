###########################################
#2023.08.11                               #
#修改邮箱展示数据库的内容                     #
#删除特定时间之前的邮箱内容（涉及发件箱，收件箱等）#
#lilei                                    #
######################################3####
# -*- coding: utf-8 -*-
import time
import DealWithTxt

#数据库导出的源文件路径
txt_db = 'D:\code\code\code2\message_ass.db.222.txt'
#处理文本的异常字符
txt_db = DealWithTxt.DealWithTxt.process_wrong_enter(txt_db)

def load_contain_insert_and_table_head_to_end_to_list():
    #装载只包含insert的list
    with open(txt_db,'r+',encoding='utf-8',errors='ignore') as file_ori:
        line_read = file_ori.readlines()
        file_ori.close()

    # 包括insert
    list_contain_sql_line = line_read[3:-9]

    # 包括表头、表尾
    list_contain_table_head_and_end = (line_read[:3]+line_read[-9:])

    return list_contain_sql_line,list_contain_table_head_and_end


'''
def load_contain_not_about_insert_to_list():
    return None   
'''



def deal_time(normal_time):
    timeArray = time.strptime(normal_time, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return timestamp

def get_deleted_and_keep_about_insert(list_contain_sql_line):
    list_deleted = []
    list_keep = []
    for i in range(0,len(list_contain_sql_line)):
        # list_about_insert = list_contain_sql_line[i].strip("\n").split(",")
        list_about_insert = list_contain_sql_line[i].split(",")

        try:
            send_time = float(list_about_insert[-6])
            reversed_time = float(list_about_insert[-5])
        except:
            print('error in string to float')
        else:
            before_set_time = '2023-06-30 0:0:0'
            before_set_unix_time = deal_time(before_set_time)
            if before_set_unix_time > send_time and before_set_unix_time > reversed_time:
                list_deleted.append(list_contain_sql_line[i]) #删除的insert内容
            else:
                list_keep.append(list_contain_sql_line[i])

    return list_deleted,list_keep






'''

def get_for_action_use():
    return None

'''


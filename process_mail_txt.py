###########################################
#2023.08.11                               #
#修改邮箱展示数据库的内容                     #
#删除特定时间之前的邮箱内容（涉及发件箱，收件箱等）#
#lilei                                    #
######################################3####
# -*- coding: utf-8 -*-
import time



# list to file
def list_to_txt(list,filepath):
    f = open(filepath, 'w')
    for line in list:
        f.write(line + '\n')
    f.close()


# file to part of list
def load_contain_insert_and_table_head_and_end_to_list(filepath):
    #装载包含 insert,head,end 的list
    with open(filepath,'r+',encoding='utf-8',errors='ignore') as file_ori:
        line_read = file_ori.readlines()
        file_ori.close()

    # 包括insert
    list_contain_insert = line_read[3:-9]

    # 包括表头、表尾 (已确认)
    list_contain_table_head = line_read[:3]
    list_contain_table_end = line_read[-9:]
    list_contain_not_head = line_read[3:]

    return list_contain_insert,list_contain_table_head,list_contain_table_end,list_contain_not_head

def load_contain_insert_to_list(filepath):
    #装载包含insert的list
    with open(filepath,'r+',encoding='utf-8',errors='ignore') as file_ori:
        line_read = file_ori.readlines()
        file_ori.close()

    # 包括insert
    list_contain_insert = line_read[3:-9]

    return list_contain_insert


def load_contain_table_head_and_end_to_list(filepath):
    # 装载包含head end 的list
    with open(filepath,'r+',encoding='utf-8',errors='ignore') as file_ori:
        line_read = file_ori.readlines()
        file_ori.close()

    # 包括表头、表尾
    list_contain_table_head = line_read[:3]
    list_contain_table_end = line_read[-9:]

    return list_contain_table_head,list_contain_table_head


def deal_time(normal_time):
    timeArray = time.strptime(normal_time, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return timestamp

def get_deleted_and_keep_about_insert(list_contain_insert):
    list_deleted = []
    list_keep = []
    for i in range(0,len(list_contain_insert)):
        # list_contain_time_about_line = list_contain_insert[i].strip("\n").split(",")
        list_contain_time_about_line = list_contain_insert[i].split(",")

        try:
            send_time = float(list_contain_time_about_line[-6])
            reversed_time = float(list_contain_time_about_line[-5])
        except:
            print('error in string to float')
        else:
            before_set_time = '2023-06-30 0:0:0'
            before_set_unix_time = deal_time(before_set_time)
            if before_set_unix_time > send_time and before_set_unix_time > reversed_time:
                list_deleted.append(list_contain_insert[i]) #删除的insert内容
            else:
                list_keep.append(list_contain_insert[i])

    return list_deleted,list_keep

#只包含特定时间之后的list
def action_do(list_contain_table_head,list_keep,list_contain_table_end):
    result_list_action_do = list_contain_table_head+list_keep+list_contain_table_end
    return result_list_action_do

#恢复包含新增的list
def action_recover_get_new_list(list_old_head, list_old_deleted, list_new_keeped+):
    result_list_recover_get_new = list_old_head + list_old_deleted + list_new_not_head
    return result_list_recover_get_new







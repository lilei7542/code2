from DealWithTxt import DealWithTxt
import process_mail_txt
import os

#数据库导出的源文件路径
filepath_ori = 'D:\code\code\code2\message_ass.db.txt.jy.0817'
#处理文本的异常字符
filepath_ori = DealWithTxt.process_wrong_enter(filepath_ori)

filepath_action_done = filepath_ori+'.action.result'
filepath_action_done = DealWithTxt.process_wrong_enter(filepath_action_done)    #设置只保留特定时间，包含新增加的内容，最后导出的文件

filepath_action_recover_done = filepath_ori+'.action.recover.result'  #恢复完成后的文件


if(os.path.exists(filepath_action_recover_done)):
    print("the program have been execute")
else:
    list_old_contain_insert,list_old_contain_table_head,list_old_contain_table_end,list_old_contain_not_head = process_mail_txt.load_contain_insert_and_table_head_and_end_to_list(filepath_ori)
    action_done_list_contain_insert,action_done_list_contain_table_head,action_done_list_contain_table_end,action_done_list_contain_not_head = process_mail_txt.load_contain_insert_and_table_head_and_end_to_list(filepath_action_done)

    list_old_deleted,list_old_keep = process_mail_txt.get_deleted_and_keep_about_insert(list_old_contain_insert)

    result_list_recover_get_new = process_mail_txt.action_recover_get_new_list(list_old_contain_table_head,list_old_deleted,list_old_contain_not_head)

    print(len(result_list_recover_get_new))

    DealWithTxt.list_to_txt(result_list_recover_get_new,filepath_action_recover_done)

    print("action_recover_done")

#需要优化， 字符格式，编码等
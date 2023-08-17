from DealWithTxt import DealWithTxt
import process_mail_txt
import os
#数据库导出的源文件路径
filepath_ori = 'D:\code\code\code2\message_ass.db.txt.jy.0817'
#处理文本的异常字符
filepath_ori = DealWithTxt.process_wrong_enter(filepath_ori)

#处理完成后的文件目录
filepath_action_done = filepath_ori+'.action.result'

if(os.path.exists(filepath_action_done)):
    print("the program have been execute")
else:
    list_contain_insert,list_contain_table_head,list_contain_table_end,list_contain_not_head = process_mail_txt.load_contain_insert_and_table_head_and_end_to_list(filepath_ori)

    list_deleted,list_keep = process_mail_txt.get_deleted_and_keep_about_insert(list_contain_insert)

    result_list_action_do = process_mail_txt.action_do(list_contain_table_head,list_keep,list_contain_table_end)

    DealWithTxt.list_to_txt(result_list_action_do,filepath_action_done)
    print("action_do_done")



####还需要再完善再优化 比如可以多次运行
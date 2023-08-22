from DealWithTxt import DealWithTxt
import process_mail_txt
from configparser import ConfigParser
from SqliteDbTxtTransfer import SqliteDbTxtTransfer
from  SwitchToDirectory import SwitchToDirectory

def action_do(user):
    parser = ConfigParser()
    parser.read('config_global.ini',encoding='utf-8')

    filepath_ori = parser.get('file','filepath_ori')  #数据库导出的源文件路径
    DealWithTxt.file_not_exist(filepath_ori)
    filepath_ori = DealWithTxt.process_wrong_enter(filepath_ori) #处理文本的异常字符

    filepath_action_done = parser.get('file','filepath_action_done')
    DealWithTxt.file_exist(filepath_action_done)

    #start to process
    list_contain_insert,list_contain_table_head,list_contain_table_end,list_contain_not_head,list_all = process_mail_txt.load_contain_insert_and_table_head_and_end_to_list(filepath_ori)

    list_deleted,list_keep = process_mail_txt.get_deleted_and_keep_about_insert(list_contain_insert)

    result_list_action_do = process_mail_txt.action_do(list_contain_table_head,list_keep,list_contain_table_end)

    filepath_action_done = DealWithTxt.list_to_txt(result_list_action_do,filepath_action_done)

    message_db_path = SwitchToDirectory.swtich_to_get_message_db_path(user)
    message_db_path_bak_for_original = message_db_path+'.bak.for.original'
    SqliteDbTxtTransfer.rename_the_file_name(message_db_path,message_db_path_bak_for_original)

    message_db_path_action_done = SqliteDbTxtTransfer.txt_to_db(filepath_action_done)
    message_db_path_action_done_now = message_db_path_action_done.replace('.action.done','')
    SqliteDbTxtTransfer.rename_the_file_name(message_db_path_action_done, message_db_path_action_done_now)


    print(user+" action_do_done")



####还需要再完善再优化 比如可以多次运
from DealWithTxt import DealWithTxt
import process_mail_txt
from configparser import ConfigParser
from SqliteDbTxtTransfer import SqliteDbTxtTransfer
from SwitchToDirectory import SwitchToDirectory


def action_recover_done(user, user_config_ini):
    parser = ConfigParser()
    parser.read(user_config_ini, encoding='utf-8')
    filepath_ori = parser.get('file', 'filepath_ori')  # 数据库导出的源文件路径
    DealWithTxt.file_not_exist(filepath_ori)
    filepath_ori = DealWithTxt.process_wrong_enter(filepath_ori)

    filepath_action_done = parser.get('file', 'filepath_action_done')
    DealWithTxt.file_not_exist(filepath_action_done)
    filepath_action_done = DealWithTxt.process_wrong_enter(filepath_action_done)  # 设置只保留特定时间，包含新增加的内容，最后导出的文件

    filepath_action_recover_at_the_moment = parser.get('file', 'filepath_action_recover_at_the_moment')
    DealWithTxt.file_not_exist(filepath_action_recover_at_the_moment)
    filepath_action_recover_at_the_moment = DealWithTxt.process_wrong_enter(filepath_action_recover_at_the_moment)

    filepath_action_recover_done = parser.get('file', 'filepath_action_recover_done')
    DealWithTxt.file_exist(filepath_action_recover_done)

    # start to process
    list_old_contain_insert, list_old_contain_table_head, list_old_contain_table_end, list_old_contain_not_head, list_old_all = process_mail_txt.load_contain_insert_and_table_head_and_end_to_list(
        filepath_ori)
    action_done_list_contain_insert, action_done_list_contain_table_head, action_done_list_contain_table_end, action_done_list_contain_not_head, list_action_done_all = process_mail_txt.load_contain_insert_and_table_head_and_end_to_list(
        filepath_action_done)

    list_old_deleted, list_old_keep = process_mail_txt.get_deleted_and_keep_about_insert(list_old_contain_insert)

    list_recover_at_the_moment = DealWithTxt.txt_to_list(filepath_action_recover_at_the_moment)

    list_new_added = process_mail_txt.get_added_about_insert(list_action_done_all, list_recover_at_the_moment)

    result_list_recover_get_new = process_mail_txt.action_recover_get_new_list(list_old_contain_table_head,
                                                                               list_old_deleted, list_old_keep,
                                                                               list_new_added,
                                                                               list_old_contain_table_end)

    filepath_action_recover_done = DealWithTxt.list_to_txt(result_list_recover_get_new, filepath_action_recover_done)

    message_db_path = SwitchToDirectory.swtich_to_get_message_db_path(user)
    message_db_path_back_for_action_recover = message_db_path.replace('.db', '.db.bak.for.action.recover')
    SqliteDbTxtTransfer.rename_the_file_name(message_db_path, message_db_path_back_for_action_recover)

    message_db_path_action_recover_done = SqliteDbTxtTransfer.txt_to_db(filepath_action_recover_done)
    message_db_path_action_recover_done_now = message_db_path_action_recover_done.replace('.action.recover.done', '')
    SqliteDbTxtTransfer.rename_the_file_name(message_db_path_action_recover_done,
                                             message_db_path_action_recover_done_now)

    print(user + " action recover done")

    # 需要优化， 字符格式，编码等

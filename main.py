from SwitchToDirectory import SwitchToDirectory
from SqliteDbTxtTransfer import SqliteDbTxtTransfer
from configparser import ConfigParser
import action_do

def main():
    parser = ConfigParser()
    parser.read('config.ini', encoding='utf-8')
    filepath_ori = parser.get('file', 'filepath_ori')

    root_base = parser.get('all_user','root_base')
    filepath_user_list = parser.get('all_user', 'filepath_user_list')

    SwitchToDirectory.swtich_to_specific_base(root_base)
    # SwitchToDirectory.swtich_to_root_base()
    # SwitchToDirectory.print_current_path()


    filepath_user_list = SwitchToDirectory.get_all_user(filepath_user_list)
    list_all_user = DealWithTxt.txt_to_list(filepath_user_list)

    for i in (len(list_all_user)):
        filepath_user_message_db = SwitchToDirectory.swtich_to_get_message_db(i)
        filepath_user_txt = SqliteDbTxtTransfer.db_to_txt(filepath_user_message_db)



if __name__ == '__main__':
    main()
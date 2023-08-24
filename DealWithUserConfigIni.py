import os
from configparser import ConfigParser
from SwitchToDirectory import SwitchToDirectory
from SqliteDbTxtTransfer import SqliteDbTxtTransfer
class DealWithUserConfigIni():

    parser = ConfigParser()
    parser.read('config_global.ini', encoding='utf-8')
    filepath_ori = parser.get('file', 'filepath_ori')

    ssmec_com = parser.get('all_user', 'ssmec_com')
    SwitchToDirectory.swtich_to_specific_base(ssmec_com)

    def mkdir_user_config_ini(user):
        os.system("cd %s" %user)
        # os.system("md %s_config.ini" %user) #for windows
        os.system("touch %s_config.ini" %user) #for linux
        current_path = SwitchToDirectory.get_current_path()
        user_config_ini = current_path+'/'+user+'_config.ini'
        return user_config_ini
    def write_file_config_to_user(user_config_ini,user):
        filepath_ori = SqliteDbTxtTransfer.db_to_txt(SwitchToDirectory.swtich_to_get_message_db_path(user))  #转化为txt
        with open(user_config_ini, 'a', encoding='utf-8', errors='ignore') as file:
            # filename.write('\n')  # 换行
            file.write('[file]')
            file.write('filepath_ori ='+filepath_ori)
            file.write('filepath_action_done =' + filepath_ori +'.action.done')
            file.write('filepath_action_recover_at_the_moment =' + filepath_ori +'.action.recover.at.the.moment')
            file.write('filepath_action_recover_done =' + filepath_ori +'.action.recover.done')

            file.close()

    # def write_sqlite_config_to_user(user_config_ini,user):  #貌似不需要

    # 考慮合併兩個函數
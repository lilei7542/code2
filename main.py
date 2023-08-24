from SwitchToDirectory import SwitchToDirectory
from configparser import ConfigParser
import action_do
from DealWithUserConfigIni import DealWithUserConfigIni

def do_action_for_all_user():
    parser = ConfigParser()
    parser.read('config_global.ini', encoding='utf-8')
    filepath_ori = parser.get('file', 'filepath_ori')

    ssmec_com = parser.get('all_user','ssmec_com')
    filepath_user_list = parser.get('all_user', 'filepath_user_list')

    SwitchToDirectory.swtich_to_specific_base(ssmec_com)

    filepath_user_list = SwitchToDirectory.get_all_user(filepath_user_list)
    list_all_user = DealWithTxt.txt_to_list(filepath_user_list)

    for user in (len(list_all_user)):
        user_config_ini = DealWithUserConfigIni.mkdir_user_config_ini(user)
        DealWithUserConfigIni.write_file_config_to_user(user_config_ini,user)
        action_do.action_do(user)



if __name__ == '__main__':
    print("chose what u want to do")
    # do_action_for_all_user()
    #
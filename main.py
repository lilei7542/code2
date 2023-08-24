from SwitchToDirectory import SwitchToDirectory
from configparser import ConfigParser
import action_do
import action_recover_done
from DealWithUserConfigIni import DealWithUserConfigIni
from DealWithTxt import DealWithTxt

#公共的獲取list for all user
parser = ConfigParser()
parser.read('config_global.ini', encoding='utf-8')

ssmec_com = parser.get('all_user', 'ssmec_com')
filepath_user_list = parser.get('all_user', 'filepath_user_list')

SwitchToDirectory.swtich_to_specific_base(ssmec_com)

filepath_user_list = SwitchToDirectory.get_all_user(filepath_user_list)
list_all_user = DealWithTxt.txt_to_list(filepath_user_list)

def do_action_for_all_user():

    for user in (len(list_all_user)):
        user_config_ini = DealWithUserConfigIni.mkdir_user_config_ini(user)
        DealWithUserConfigIni.write_file_config_to_user(user_config_ini,user)
        action_do.action_do(user)



def do_action_recover_for_all_user():

    for user in (len(list_all_user)):
        # user_config_ini = DealWithUserConfigIni.mkdir_user_config_ini(user)
        # DealWithUserConfigIni.write_file_config_to_user(user_config_ini,user)
        action_recover_done.action_recover_done(user)






if __name__ == '__main__':
    print("chose what u want to do")
    # do_action_for_all_user()
    # do_action_recover_for_all_user()
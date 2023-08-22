import os

class SwitchToDirectory():


    def swtich_to_root_base():
        os.system("cd")

    def swtich_to_specific_base(specific_base):
        os.system("cd %s" %specific_base)

    def get_all_user(filepath_user_list):
        os.system('ls -I *.tar >%s' %(filepath_user_list))
        return filepath_user_list

    def switch_to_user_base(user):
        swtich_to_root_base()
        os.system("cd account")
        os.system("cd %s" %(user))


    def get_current_path():
        return  (os.system('pwd'))

    def swtich_to_get_message_db_path(user):
        swtich_to_root_base()
        os.system("cd account")
        os.system("cd %s" %(user))
        os.system("cd ts")
        path = os.system("pwd")
        return path+"/message_ass.db"


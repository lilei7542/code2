import os

class SqliteDbTxtTransfer():

    def db_to_txt(filename_db,filename_txt):
        os.system("sqlite3 %s .dump > %s" %(filename_db,filename_txt))
        return filename_txt

    def txt_to_db(filename_db,filename_txt):
        os.system("sqlite3 %s < %s" %(filename_db,filename_txt))
        return filename_db




class SqliteDbTxtTransfer():


    def db_to_txt(filename_db):
        filename_txt = filename_db.replace('.db','.txt')
        os.system("sqlite3 %s .dump > %s" %(filename_db,filename_txt))
        return filename_txt

    def txt_to_db(filename_txt):
        filename_db = filename_txt.replace('.txt','.db')
        os.system("sqlite3 %s < %s" %(filename_db,filename_txt))
        return filename_db
    def rename_the_file_name(file1,file2):
        os.system('mv %s %s'%(file1,file2))



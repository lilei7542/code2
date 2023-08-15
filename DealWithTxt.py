# -*- coding: utf-8 -*-
import os

class DealWithTxt(object):

    def process_wrong_enter(path_from):
        path_out = path_from+'.tmp'

        from_file = open(path_from, 'r+', encoding='utf-8',errors='ignore')
        out_file = open(path_out, 'w', encoding='utf-8',errors='ignore')

        #处理异常换行
        tmp = from_file.read().replace('\n <',' <')

        out_file.writelines(tmp)
        out_file.flush()
        out_file.close()
        from_file.close()

        #重命名，删除
        os.remove(path_from)
        os.rename(path_out,path_from)

        return path_from




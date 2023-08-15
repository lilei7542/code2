class DealWithTxt(list):

    def compare_list_for_all_between_part(list_all,list_part_of):
        # 保留剩下的
        list_result = []
        for i in range(len(list_all)):
            a = list_all[i]
            for j in range(len((list_part_of))):
                b = list_part_of[j]
                if b != a :
                    list_result.
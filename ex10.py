def radix_sort(unsorted):
    size_unsorted = len(unsorted)
    final_sorted = []
    digit = 1
    finished_num = 0
    while finished_num < size_unsorted:
        sorted_list = []
        finished_num = 0
        num_bin = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
        num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for index in range(len(unsorted)):
            str_num = str(unsorted[index])
            if len(str_num) >= digit:
                for num in num_list:
                    if int(str_num[-1 * digit]) == num:
                        num_bin[num].append(unsorted[index])
            else:
                num_bin[0].append(unsorted[index])
                finished_num += 1
        for key in num_list:
            for element in num_bin[key]:
                sorted_list.append(element)
        unsorted = sorted_list
        digit += 1
    return sorted_list

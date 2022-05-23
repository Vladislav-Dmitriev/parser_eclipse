import numpy as np


def make_list_for_dataframe(list_3,
                            key_words_for_delete=["WEFAC"],
                            key_words=['DATES', 'WEFAC', 'COMPDAT', 'COMPDATL', 'END']):
    """
    Function for parsing data after validation
    :param list_3:
    :param key_words_for_delete:
    :param key_words:
    :return:
    """
    final_list = []
    list_words_for_delete = ['DATES', 'END']
    for word in key_words_for_delete:
        list_words_for_delete.append(word)
    key_words_for_parsing = key_words[:]
    for word in list_words_for_delete:
        key_words_for_parsing.remove(word)
    for string in list_3:
        if 'DATES' in string and len(string) == 2:
            final_list.append([string[1]] + [np.nan] * 15)
        if any(element in string for element in key_words_for_parsing):
            if 'DATES' in string:
                indices = [i for i, x in enumerate(string) if x in key_words_for_parsing]
                for ind in indices:
                    i = 1
                    while ind + i not in indices and (ind + i) <= (len(string) - 1):
                        l = string[ind + i].split()
                        if string[ind] == "COMPDAT":
                            l.insert(0, string[1])
                            l.insert(2, np.nan)
                            final_list.append(l)
                        elif string[ind] == "COMPDATL":
                            l.insert(0, string[1])
                            final_list.append(l)
                        i += 1
            if 'DATES' not in string:
                indices = [i for i, x in enumerate(string) if x in key_words_for_parsing]
                for ind in indices:
                    i = 1
                    while ind + i not in indices and (ind + i) <= (len(string) - 1):
                        l = string[ind + i].split()
                        if string[ind] == "COMPDAT":
                            l.insert(0, np.nan)
                            l.insert(2, np.nan)
                            final_list.append(l)
                        elif string[ind] == "COMPDATL":
                            l.insert(0, np.nan)
                            final_list.append(l)
                        i += 1
    return final_list

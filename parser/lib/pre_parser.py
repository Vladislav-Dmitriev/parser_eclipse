import re


def init_validation(lines):
    """
    Data cleaning function
    :param lines:
    :return:
    """
    list_1 = []

    # Чистка данных
    for line in lines:
        line_new = re.sub(r'\t', ' ', line)
        line_new = re.sub(r'/', '', line_new)
        line_new = re.sub(r"'", '', line_new)
        line_new = line_new.split("--")[0]
        line_new = line_new.strip()
        line_new = re.sub(" +", " ", line_new)
        line_new = line_new.replace('1*', 'DEFAULT')
        line_new = line_new.replace('3*', 'DEFAULT DEFAULT DEFAULT')
        if line_new and line_new.strip():
            list_1.append(line_new)
    return list_1


def validation(lines,
               key_words_for_delete=["WEFAC"],
               key_words=['DATES', 'WEFAC', 'COMPDAT', 'COMPDATL', 'END']):
    """
    Main data cleaning function
    :param lines:
    :param key_words_for_delete:
    :param key_words:
    :return:
    """
    list_1 = init_validation(lines)
    list_data = []
    for index, elem in enumerate(list_1):
        f = re.findall(r'[0-9][0-9]\s[A-Z]+\s[0-9]{4}', elem)
        if f:
            list_data.append(index)
    for number in range(len(list_data) - 1):
        if list_data[number + 1] - list_data[number] == 1:
            list_1.insert(list_data[number + 1], 'DATES')

    init_key_words = key_words
    init_key_words_final = init_key_words[:]
    delete_key_word = key_words_for_delete

    for key_word in delete_key_word:
        init_key_words_final.remove(key_word)

    # Удаление WEFAC
    list_2 = list_1[:]
    indices = [i for i, x in enumerate(list_1) if x in delete_key_word]
    list_for_drop_main = []
    for index in indices:
        list_for_drop = []
        i = index
        while list_1[i] not in init_key_words_final:
            list_for_drop.append(i)
            list_for_drop_main.append(list_for_drop)
            new_list = [item for sublist in list_for_drop_main for item in sublist]
            new_list = sorted(list(set(new_list)))
            i += 1
    for index, elem in enumerate(new_list):
        list_2.pop(elem - index)

    # Проврека ключевого слова END (Слайс до первого слова END) (Конец работы программы)
    list_2 = list_2[:list_2.index('END')]

    # Ищем первое ключевое слово (Начало работы программы)
    start_list = []
    init_key_words_final.remove('END')
    for start in init_key_words_final:
        start_list.append(list_1.index(start))
    start_index = min(start_list)

    # Сепарация списка на сегменты
    list_3 = []
    indices = [i for i, x in enumerate(list_2) if x == 'DATES']
    indices.insert(0, start_index)
    indices.append(len(list_2))
    for index in range(len(indices) - 1):
        list_3.append(list_2[indices[index]:indices[index + 1]])
    return list_3

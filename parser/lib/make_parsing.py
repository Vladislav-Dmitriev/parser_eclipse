from lib.read_file import read_file  # Чтение файла
from lib.pre_parser import validation  # Фильтрация данных
from lib.main_parser import make_list_for_dataframe  # Создание списка удобного вида для парсинга в датафрейм
from lib.post_parser import make_dataframe  # Создание датафрейма


def make_parsing(filename, key_words_for_delete=["WEFAC"]):
    """
    File parsing function
    :param filename:
    :param key_words_for_delete:
    :return:
    """
    list_init = read_file(filename)
    list_clean = validation(list_init, key_words_for_delete)
    list_for_df = make_list_for_dataframe(list_clean, key_words_for_delete)
    final_df = make_dataframe(list_for_df)
    return final_df

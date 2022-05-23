import pytest
import pandas as pd
import numpy as np
from lib.read_file import read_file  # Чтение файла
from lib.pre_parser import validation  # Фильтрация данных
from lib.pre_parser import init_validation  # Внутренняя функция validation()
from lib.main_parser import make_list_for_dataframe  # Создание списка удобного вида для парсинга в датафрейм
from lib.post_parser import make_dataframe  # Создание датафрейма


@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_read_file(filename):
    """
    Check type of data after function read_file()
    :param filename:
    :return:
    """
    test_filename = read_file(filename)
    assert type(test_filename) == list


def test_pre_parser_1():
    """
    Check correctness of data cleansing
    :return:
    """
    input = ["01 JUN 2018 /"]
    output = ["01 JUN 2018"]
    assert init_validation(input) == output


def test_pre_parser_2():
    """
    Check correctness of data cleansing
    :return:
    """
    input = ["'W3' 'LGR1' 10 10  2   2 	OPEN 	1* 	1	2 	1 	3* 			1.0918 /"]
    output = ['W3 LGR1 10 10 2 2 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 1.0918']
    assert init_validation(input) == output


@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_pre_parser_3(filename):
    """
    Check correctness of replacing a number with * in data
    :param filename:
    :return:
    """
    test_filename = read_file(filename)
    test_list = [item for i in validation(test_filename) for item in i]
    assert '1*' or '2*' not in test_list


@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_pre_parser_3(filename):
    """
    Check the correct operation of the function with different key_words_for_delete
    :param filename:
    :return:
    """
    test_filename = read_file(filename)
    test_list_1 = [item for i in validation(test_filename, key_words_for_delete=["WEFAC"]) for item in i]
    test_list_2 = [item for i in validation(test_filename, key_words_for_delete=["WEFAC", 'COMPDAT']) for item in i]
    test_list_3 = [item for i in validation(test_filename, key_words_for_delete=["WEFAC", 'COMPDAT', 'COMPDATL']) for
                   item in i]
    assert 'COMPDAT' and 'COMPDATL' in test_list_1 and 'WEFAC' not in test_list_1
    assert 'COMPDAT' and 'WEFAC' not in test_list_2 and 'COMPDATL' in test_list_2
    assert 'COMPDAT' and 'COMPDATL' and 'WEFAC' not in test_list_3


@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_main_parser(filename):
    """
    Check are there np.nans in the data
    :param filename:
    :return:
    """
    list_after_main_parser = make_list_for_dataframe(validation(read_file(filename)))
    test_list = [item for i in list_after_main_parser for item in i]
    assert np.nan in test_list


@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_post_parsing_1(filename):
    """
    Check type of data after function make_dataframe()
    :param filename:
    :return:
    """
    list_after_main_parser = make_list_for_dataframe(validation(read_file(filename)))
    data_frame = make_dataframe(list_after_main_parser)
    assert type(data_frame) == pd.core.frame.DataFrame


@pytest.mark.parametrize('filename, columns', [('input_data_test/test_schedule.inc', [
    'Date',
    'Well name',
    'Local grid name',
    'I',
    'J',
    'K upper',
    'K lower',
    'Flag on connection',
    'Saturation table',
    'Transmissibility factor',
    'Well bore diameter',
    'Effective Kh',
    'Skin factor',
    'D-factor',
    'Dir_well_penetrates_grid_block',
    'Press_eq_radius'
])])
def test_post_parsing_2(filename, columns):
    """
    Check columns name
    :param filename:
    :param columns:
    :return:
    """
    list_after_main_parser = make_list_for_dataframe(validation(read_file(filename)))
    data_frame = make_dataframe(list_after_main_parser)
    assert list(data_frame.columns) == columns

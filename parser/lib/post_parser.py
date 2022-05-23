import pandas as pd


def make_dataframe(final_list):
    """
    The function creates a dataframe from the input list
    :param final_list:
    :return:
    """
    columns_name = [
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
    ]
    output_df = pd.DataFrame(final_list, columns=columns_name)
    return output_df

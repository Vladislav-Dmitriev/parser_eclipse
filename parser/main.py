from lib.make_parsing import make_parsing

filename = 'data/input_data/test_schedule.inc'

if __name__ == '__main__':
    output_df = make_parsing(filename, key_words_for_delete=["WEFAC"])
    output_df.to_excel('data/output_data/output.xlsx')

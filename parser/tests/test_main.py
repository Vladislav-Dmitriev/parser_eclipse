import pytest
import numpy as np
from lib.make_parsing import make_parsing


class TestUnitParser:
    @pytest.fixture
    def set_up(self):
        """
        Prepares info for reference input file(s)
        @return: None
        """
        self.input_file = 'input_data_test/test_schedule.inc'  # Входные данные для парсинга

        self.parse_list_output_reference = [
            [np.nan, 'W1', np.nan, '10', '10', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '1.0'],
            [np.nan, 'W2', np.nan, '32', '10', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '2.0'],
            [np.nan, 'W3', np.nan, '5', '36', '2', '2', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '3.0'],
            [np.nan, 'W4', np.nan, '40', '30', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '4.0'],
            [np.nan, 'W5', np.nan, '21', '21', '4', '4', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '5.0'],
            ['01 JUN 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan, np.nan, np.nan],
            ['01 JUL 2018', 'W3', np.nan, '32', '10', '1', '1', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '1.0718'],
            ['01 JUL 2018', 'W5', np.nan, '21', '21', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '5.0'],
            ['01 AUG 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan, np.nan, np.nan],
            ['01 SEP 2018', 'W1', np.nan, '10', '10', '2', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '1.0918'],
            ['01 SEP 2018', 'W2', np.nan, '32', '10', '1', '2', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '2.0'],
            ['01 SEP 2018', 'W3', 'LGR1', '10', '10', '2', '2', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '1.0918'],
            ['01 OCT 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan, np.nan, np.nan],
            ['01 NOV 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan, np.nan, np.nan],
            ['01 DEC 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan, np.nan, np.nan]]

    def test_parse_schedule(self, set_up):
        """
        Check the correctness of the parser output
        :param set_up:
        :return:
        """
        assert make_parsing(self.input_file).values.tolist() == self.parse_list_output_reference

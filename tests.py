import unittest
from time_duration import calc_diff


class TestCase(unittest.TestCase):
    def test1(self):
        time1 = '8:15'
        period1 = 'AM'
        time2 = '9:00'
        period2 = 'AM'
        expected = "0:45:00"
        self.assertEqual(str(calc_diff(time1, period1, time2, period2)),
                         expected)

    def test2(self):
        time1 = '8:15'
        period1 = 'AM'
        time2 = '9:00'
        period2 = 'PM'
        expected = "12:45:00"
        self.assertEqual(str(calc_diff(time1, period1, time2, period2)),
                         expected)

    def test3(self):
        time1 = '11:15'
        period1 = 'AM'
        time2 = '1:00'
        period2 = 'AM'
        expected = "13:45:00"
        print(str(calc_diff(time1, period1, time2, period2)))
        self.assertEqual(str(calc_diff(time1, period1, time2, period2)),
                         expected)

    def test4(self):
        time1 = '10:15'
        period1 = 'PM'
        time2 = '2:00'
        period2 = 'AM'
        expected = "3:45:00"
        print(str(calc_diff(time1, period1, time2, period2)))
        self.assertEqual(str(calc_diff(time1, period1, time2, period2)),
                         expected)


if __name__ == '__main__':
    unittest.main()

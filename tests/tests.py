import unittest
from argparse import Namespace
import datetime as dt
from timediff.__main__ import main, calc_diff


class TestCase(unittest.TestCase):
    def test1(self):
        args = Namespace(time1='8:15', period1='AM', time2='9:00',
                         period2='AM')
        expected = dt.timedelta(hours=0, minutes=45)
        self.assertEqual(calc_diff(args), expected)

    def test2(self):
        args = Namespace(time1='8:15', period1='AM', time2='9:00',
                         period2='PM')
        expected = dt.timedelta(hours=12, minutes=45)
        self.assertEqual(calc_diff(args), expected)

    def test3(self):
        args = Namespace(time1='11:15', period1='AM', time2='1:00',
                         period2='AM')
        expected = dt.timedelta(hours=13, minutes=45)
        self.assertEqual(calc_diff(args), expected)

    def test4(self):
        args = Namespace(time1='10:15', period1='PM', time2='2:00',
                         period2='AM')
        expected = dt.timedelta(hours=3, minutes=45)
        self.assertEqual(calc_diff(args), expected)


if __name__ == '__main__':
    unittest.main()

import unittest
import HW1

class testCaseleapYear(unittest.TestCase):
    def test_not100(self):
        self.assertEqual (HW1.leapYear(1939), False)
    def test_not1002(self):
        self.assertEqual (HW1.leapYear(1720), True)
    def test_div100(self):
        self.assertEqual (HW1.leapYear(1900), False)
    def test_div400(self):
        self.assertEqual (HW1.leapYear(2000), True)
    def test_zero(self):
        self.assertEqual (HW1.leapYear(0), True)


if __name__ == "__main__":
    unittest.main()
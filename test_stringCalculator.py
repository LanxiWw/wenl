import unittest
from stringCalculator import stringCalculator

class test_stringCalculator(unittest.TestCase):

    # task  1 & 2
    def test_string1(self):
        calculator = stringCalculator()
        self.assertEqual(calculator.string1(""), 0)
        self.assertEqual(calculator.string1("2"), 2)
        self.assertEqual(calculator.string1("-2"), -2)


    def test_string2(self):
        calculator = stringCalculator()
        self.assertEqual(calculator.string2("1,2"), 3)
        #self.assertEqual(calculator.string2("2,2"), 22)


    def test_string3(self):
        calculator = stringCalculator()
        self.assertEqual(calculator.string3("1\n2"), 3)
        #self.assertEqual(calculator.string3("2\n3"), 6)

    def test_string4(self):
        calculator = stringCalculator()
        self.assertEqual(calculator.string4("7,7,7"), 21)
        #self.assertEqual(calculator.string4("1,10,20"), 21)

    def test_string6(self):
        calculator = stringCalculator()
        self.assertEqual(calculator.string6("-1"), None)

    def test_string7(self):
        calculator = stringCalculator()
        self.assertEqual(calculator.string7("1200", "100"), 100)
        self.assertEqual(calculator.string7("120", "100"), (120, 100))
        #self.assertEqual(calculator.string7("120", "1002"), 1002)





    if __name__ == '__main__':
        unittest.main()
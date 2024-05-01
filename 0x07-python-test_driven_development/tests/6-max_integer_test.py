import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    unittest to test max_integer function
    """
    def test_max_positive(self):
        """To find max positive number"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 11, 24, 20]), 24)

    def test_negative(self):
        """To find max negative number"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -200, -1, -29]), -1)

    def test_mixed_number(self):
        """To find max number in mixed list"""
        self.assertEqual(max_integer([-12, 20, 24, -6]), 24)
        self.assertEqual(max_integer([-24, 2, 8, -100]), 8)

    def test_float(self):
        """To find in a list of floats"""
        self.assertEqual(max_integer([-0.5, -1.5, -2.5, 1]), 1)
        self.assertEqual(max_integer([1.5, -2.5, -0.5, 2.5]), 2.5)

    def test_empty_list(self):
        """To check whether list is empty"""
        self.assertIsNone(max_integer([]))

    def single_element(self):
        """check in list with single element"""
        self.assertEqual(max_integer([0.1]), 0.1)

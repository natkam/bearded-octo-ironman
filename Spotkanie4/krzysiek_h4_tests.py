import unittest
from krzysiek_rev import rev
from krzysiek_brackets import valid_brackets

class TestHomeworkFour(unittest.TestCase):
        def test_list_reversion(self):
            list_len_two = [1, 2]
            list_len_three = [1, 2, 3]
            my_list = [1 ,2 ,3 ,4]
            another = [i for i in range(1 , 101)]
            self.assertEqual(rev(list_len_two), [2, 1])
            self.assertEqual(rev(list_len_three), [3, 2, 1])
            self.assertEqual(rev(my_list), [4, 3, 2, 1])
            self.assertEqual(rev(another), [i for i in range(100, 0, -1)])

        def test_valid_brackets(self):
            self.assertTrue(valid_brackets('(([[{}]]))'))
            self.assertFalse(valid_brackets('(){[}]()'))
            self.assertTrue(valid_brackets('{(){}[]}'))
            self.assertFalse(valid_brackets('{}<{'))
            self.assertFalse(valid_brackets('[}'))

if __name__ == '__main__':
    unittest.main()

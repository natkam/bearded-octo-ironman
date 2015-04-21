import unittest

def bubble_sort(numbers):
    sort = False
    while not sort:
        sort = True
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                sort = False
    return numbers

class BubbleSortTest(unittest.TestCase):
    def setUp(self):
        self.nums = [2,1,4,9,7,6]
        
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.nums), [1,2,4,6,7,9])


if __name__ == '__main__':
    unittest.main()

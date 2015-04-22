import unittest
import krzysiek_ksiazka as ksiazka


class PhonebookTests(unittest.TestCase):
    def setUp(self):
        ksiazka.init()
        self.phonebook = ksiazka.phonebook
        
    def test_add_number(self):
        ksiazka.add_number('Adam','Test',123456789)
        self.assertDictEqual(self.phonebook, {'Test':{'Adam':[123456789]}})
        
    def test_clean_phonebook(self):
        ksiazka.add_number('Maria','Kowalska',123456789)
        ksiazka.clean()
        self.assertDictEqual(self.phonebook, {})
        
    def test_search_phonebook(self):
        ksiazka.add_number('Adam','Test',123456789)
        ksiazka.add_number('Janina','Test',987654321)
        search_generator = ksiazka.search('Test')
        self.assertEqual(next(search_generator), 123456789)
        self.assertEqual(next(search_generator), 987654321)
        numbers = (self.phonebook['Test']['Adam'][0], 
                   self.phonebook['Test']['Janina'][0])
        for number in ksiazka.search('Test'):
            self.assertIn(number, numbers)
        
    def test_fail_search(self):
        with self.assertRaisesRegex(StopIteration, 'Empty'):
            next(ksiazka.search('Empty'))
        
if __name__ == '__main__':
    unittest.main()

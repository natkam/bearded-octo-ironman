import unittest
import ksiazka


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
        #self.assertEqual(next(ksiazka.search('Test')), 123456789)
        #next(ksiazka.search('Test'))
        #self.assertEqual(next(ksiazka.search('Test')), 987654321)
        numbers = (self.phonebook['Test']['Adam'][0], 
                   self.phonebook['Test']['Janina'][0])
        for number in ksiazka.search('Test'):
            self.assertIn(number, numbers)
        
    def test_fail_search(self):
        # exception should occur before iterating
        with self.assertRaisesRegex(KeyError, 'Empty'):
            next(ksiazka.search('Empty'))
        
if __name__ == '__main__':
    unittest.main()

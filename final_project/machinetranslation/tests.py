import unittest
from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_french_null_english(self):
        self.assertNotEqual(french_to_english('None'), '')
    def test_english_null_french(self):
        self.assertNotEqual(english_to_french('None'), '')
    def test_hello_2bonjour(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  
    def test_bonjour_2hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')      
    
unittest.main()
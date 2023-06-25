import unittest
from translator import english_to_french, french_to_english

class TestMyModules(unittest.TestCase):
    ''' Test class for translator module '''

    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour', 'English translte Error')
        self.assertEqual(english_to_french('Banana'), 'Banane', 'English translte Error')
        self.assertEqual(english_to_french('Monkey'), 'Singe', 'English translte Error')
        self.assertEqual(english_to_french('Car'), 'Voiture', 'English translte Error')

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello', 'Franch translte Error')
        self.assertEqual(french_to_english('Banane'), 'Banana', 'Franch translte Error')
        self.assertEqual(french_to_english('Singe'), 'Monkey', 'Franch translte Error')
        self.assertEqual(french_to_english('Voiture'), 'Car', 'Franch translte Error')
        
unittest.main()

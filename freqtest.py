from importguard import freq
import unittest


class TestFreq(unittest.TestCase):
        
    def test_dict(self):
        d={'a': 2, 'b': 2, ' ': 1, '?': 1}
        s="abba ?"
        self.assertDictEqual(d,freq(s))




if __name__ == "__main__":
    unittest.main()

from importguard import palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def testIsPalindrome(self):
        pl = "malayalam"
        self.assertTrue(palindrome(pl))

    def testIsNotPanagram(self):
        pl = "malay"
        self.assertFalse(palindrome(pl))
    
    def testNullInput(self):
        ret = palindrome("")
        self.assertTrue(ret)


if __name__ == "__main__":
    unittest.main()

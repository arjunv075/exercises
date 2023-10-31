import unittest

def freq(s):
    d={}
    s=s.lower()
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

class TestFreq(unittest.TestCase):
    def testIsFreq(self):
        s = "malayalam"
        self.assertTrue(freq(s))
        
    
    def testNullInput(self):
        ret = freq("")
        self.assertFalse(ret)


if __name__ == "__main__":
    unittest.main()
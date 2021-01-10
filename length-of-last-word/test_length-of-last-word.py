import unittest
import lengthoflastword

class MyTestCase(unittest.TestCase):
    def test_lengthoflastword(self):
        length = lengthoflastword.Solution()
        s = "fff"
        self.assertEqual(length.lengthOfLastWord(s),0)


if __name__ == '__main__':
    unittest.main()

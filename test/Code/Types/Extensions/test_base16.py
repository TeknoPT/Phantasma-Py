import unittest

from phantasma_py.Types.Extensions import Base16

class TestBase16(unittest.TestCase):
    def test_something(self):
        encodedText = Base16.encode("Test")
        print(encodedText)

        decodeText = Base16.decode(encodedText)
        print(decodeText)

        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

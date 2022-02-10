import unittest

import main


class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.hellowword("Test")
        self.assertEqual(ret, "hello world: Test")  # test area


if __name__ == "__main__":
    unittest.main()

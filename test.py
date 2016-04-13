import unittest
import os
from app import App

class TestSuite(unittest.TestCase):
    def test(self):
        app = App()
        if os.environ.get("run") == "all":
            self.failIf(app.multiply(2,3) != 6)
            self.failIf(app.sum(1,1) != 2)
            self.failIf(app.diff(1,1) != 0)
            self.failIf(app.divide(1,1) != 1)
        else:
            self.failIf(app.sum(1,1) != 2)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

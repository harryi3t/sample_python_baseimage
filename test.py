import unittest
from app import App

class TestSuite(unittest.TestCase):
    def test(self):
        app = App()
        self.failIf(app.calculate(1,2) != 3)
    def test2(self):
        app = App()
        self.failIf(app.calculate(1,2) != 5)
    def test3(self):
        app = App()
        self.failIf(app.calculate(1,2) != 3)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

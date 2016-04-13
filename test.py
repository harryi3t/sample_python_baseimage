import unittest
import os
from file1 import App1
from file2 import App2

class TestSuite(unittest.TestCase):
    def testSum1(self):
        app = App1()
        run = os.environ.get("run")
        if run == "app1" or run == "all" :
            self.failIf(app.sum(10,2) != 12)
    def testDiff1(self):
        app = App1()
        run = os.environ.get("run")
        if run == "app1" or run == "all" :
            self.failIf(app.diff(10,2) != 8)
    def testMultiply1(self):
        app = App1()
        run = os.environ.get("run")
        if run == "app1" or run == "all" :
            self.failIf(app.multiply(10,2) != 20)
    def testDivide1(self):
        app = App1()
        run = os.environ.get("run")
        if run == "app1" or run == "all" :
            self.failIf(app.divide(10,2) != 5)

    def testSum2(self):
        app = App2()
        run = os.environ.get("run")
        if run == "app2" or run == "all" :
            self.failIf(app.sum(10,2) != 12)
    def testDiff2(self):
        app = App2()
        run = os.environ.get("run")
        if run == "app2" or run == "all" :
            self.failIf(app.diff(10,2) != 8)
    def testMultiply2(self):
        app = App2()
        run = os.environ.get("run")
        if run == "app2" or run == "all" :
            self.failIf(app.multiply(10,2) != 20)
    def testDivide2(self):
        app = App2()
        run = os.environ.get("run")
        if run == "app2" or run == "all" :
            self.failIf(app.divide(10,2) != 5)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

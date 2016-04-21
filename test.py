import unittest
import os
from file1 import App1
from file2 import App2

class TestSuite(unittest.TestCase):
	def test1(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)
	def test2(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)
	def test3(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)
	def test4(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)
	def test5(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)
	def test6(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)
	def test7(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)
	def test8(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)
	def test9(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)
	def test10(self):
	   app = App()
	   self.failIf(app.calculate(0,0) != 1)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

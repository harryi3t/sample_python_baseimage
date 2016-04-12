class App():
    def __init__(self):
        self.var1 = 15

    def calculate(self, a, b):
        return a+b;

    def retrieve(self):
        return self.result

if __name__ == "__main__":
    app = App()
    app.calculate()
    print(app.retrieve)

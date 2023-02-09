import file3

class B():
    def foo(self):
        print(__name__)
if __name__ == "__main__":
    b = B()
    b.foo()

    p2 = file3.People("Ani")
    p2.info()

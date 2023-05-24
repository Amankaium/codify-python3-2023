def my_decorator(some_function):  # two
    def wrapper():
        a = 7
        print(a)
        some_function()  # two()
        b = 44
        print(b + 5)
    return wrapper


@my_decorator
def one():
    print("first function")

@my_decorator
def two():
    print("second one")


@my_decorator
def test_1():
    print("hello world")


def dec_2(fn):
    def test_1():
        print("hello world")
        fn()
    return test_1

# two()
# one() # my_decorator(one)()
# my_decorator(two)()  # wrapper()
test_1()

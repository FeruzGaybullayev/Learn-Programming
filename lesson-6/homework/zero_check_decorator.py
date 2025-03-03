# Zero Check Decorator
def check(func):
    def wrapper(a, b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Detorminator can't be zero")
    return wrapper

@check
def div(a, b):
    return a/b

print(div(6, 2))
print(div(6, 0))
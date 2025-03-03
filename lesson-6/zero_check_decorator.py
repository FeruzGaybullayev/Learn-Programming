# Zero Check Decorator 
def check(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            print('Detorminator can\'t be zero')
    return wrapper

@check
def div(a, b):
    return a/b

print(div(5, 4))
print(div(9, 0))
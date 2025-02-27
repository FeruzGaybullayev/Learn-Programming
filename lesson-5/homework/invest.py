# n this challenge, you will write a program called invest.py that tracks the growing amount of an investment over time.

def invest(amount, rate, years):
    for years in range(1, years + 1):
        amount += amount * rate 
        print(f'year {years}: {amount:.2f}')
    return ''

# For example, calling invest(100, .05, 4) should print the following:
my_dep = invest(100, .05, 4)
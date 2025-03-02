# Task 3
# A factor of a positive integer n is any positive integer less than or equal to n that divides n with no remainder.

number = input('Enter a positive integer: ')
for num in range(1, number+1):
  if bunber % num == 0:
    print(f'{num} is factor of {number}')

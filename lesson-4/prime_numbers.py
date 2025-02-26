prime_numbers = set()

for num in range(2, 100):
    is_prime = True
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            is_prime = False
            break
    if is_prime:
            prime_numbers.add(num)
print(prime_numbers)
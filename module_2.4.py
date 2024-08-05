numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for number in numbers:
    if number == 2 or number == 3:
        prime.append(number)
        continue
    isPrime = True
    for i in range(1, number):
        if number % i == 0 and i != 1 and i != number:
            not_prime.append(number)
            isPrime = False
            break
    if isPrime and number != 1:
        prime.append(number)

print(f"prime\n{prime}")
print(f"not prime\n{not_prime}")

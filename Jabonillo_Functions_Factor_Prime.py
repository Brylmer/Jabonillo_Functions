def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                print(f"The smallest factor of {n} is: {i}")
                break

def find_prime_numbers_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    print(f"Prime numbers in the range [{start}, {end}]: {primes}")

try:
    choice = int(input("Choose an option:\n1. Find smallest factor of a number\n2. Find prime numbers in a range\nEnter choice (1 or 2): "))

    if choice == 1:
        n = int(input("Enter an integer (>= 2): "))
        find_smallest_factor(n)
    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        find_prime_numbers_in_range(start, end)
    else:
        print("Invalid choice. Please enter 1 or 2.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

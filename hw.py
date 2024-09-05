# -*- coding: utf-8 -*-
"""hw.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FzDUAC8eDd3foAZli0fvv0d96hcGCXDH
"""

# Input three float numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate addition and average
addition = num1 + num2 + num3
average = addition / 3

# Print results
print(f"Addition: {addition}")
print(f"Average: {average}")

import math

radius = 6
volume = (4/3) * math.pi * (radius ** 3)

print(f"Volume of the sphere: {volume:.2f} cubic cm")

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)

print(f"Area of the circle: {area:.2f} square units")

# Input principal, rate, and time
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

# Calculate simple interest
interest = (principal * rate * time) / 100

print(f"Simple Interest: {interest:.2f}")

# Input two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Swap values
a, b = b, a

print(f"Swapped values: a = {a}, b = {b}")

# Input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

days = int(input("Enter number of days: "))

years = days // 365
days %= 365
months = days // 30
days %= 30
weeks = days // 7
days %= 7

print(f"{years} years, {months} months, {weeks} weeks, {days} days")

G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2

m1 = float(input("Enter mass of first object (kg): "))
m2 = float(input("Enter mass of second object (kg): "))
d = float(input("Enter distance between objects (m): "))

force = G * (m1 * m2) / (d ** 2)

print(f"Gravitational force: {force:.2e} N")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

num = int(input("Enter a number: "))
difference = num - 15

if num > 15:
    print(f"Two times of difference: {2 * difference}")
else:
    print(f"Four times of difference: {4 * difference}")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = max(a, b, c)
print(f"The largest number is: {largest}")

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(4)]
average = sum(marks) / 4

if average >= 75:
    grade = 'A'
elif average >= 60:
    grade = 'B'
elif average >= 40:
    grade = 'C'
else:
    grade = 'D'

print(f"Average marks: {average:.2f}")
print(f"Grade: {grade}")

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    result = num1 / num2
else:
    result = "Invalid Input"

print(f"Result: {result}")

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots are real and different. Root1 = {root1}, Root2 = {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"Root is real and same. Root = {root}")
else:
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(-discriminant) / (2 * a)
    print(f"Roots are complex and different. Root1 = {realPart} + {imaginaryPart}i, Root2 = {realPart} - {imaginaryPart}i")

n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(i)

n = int(input("Enter a number: "))

sum_n = n * (n + 1) // 2
print(f"Sum of natural numbers up to {n} is: {sum_n}")

num = input("Enter a number: ")

sum_digits = sum(int(digit) for digit in num)
print(f"Sum of digits: {sum_digits}")

num = int(input("Enter a number: "))

factors = [i for i in range(1, num + 1) if num % i == 0]
print(f"Factors of {num}: {factors}")

num = input("Enter a number: ")

reverse_num = num[::-1]
print(f"Reverse of the number: {reverse_num}")

import math

num = int(input("Enter a number: "))
factorial = math.factorial(num)

print(f"Factorial of {num} is: {factorial}")

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

# Example usage
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return num == sum_of_powers

# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Example usage
n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
print(fibonacci(n))

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage
number = int(input("Enter a number to print its multiplication table: "))
multiplication_table(number)

user_input = input("Enter elements separated by spaces: ")
input_list = user_input.split()
print("The list is:", input_list)

def find_average(numbers):
    return sum(numbers) / len(numbers)

# Example usage
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(float, user_input.split()))
average = find_average(numbers)
print("The average is:", average)

def find_largest(numbers):
    return max(numbers)

# Example usage
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(float, user_input.split()))
largest = find_largest(numbers)
print("The largest number is:", largest)

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage
user_input = input("Enter numbers separated by spaces: ")
arr = list(map(int, user_input.split()))
target = int(input("Enter the number to search for: "))
index = linear_search(arr, target)
if index != -1:
    print(f"{target} found at index {index}.")
else:
    print(f"{target} not found in the list.")

print("Enter lines of text (type 'END' to finish):")
lines = []
while True:
    line = input()
    if line == 'END':
        break
    lines.append(line.upper())

print("\nCapitalized lines:")
for line in lines:
    print(line)

user_input = input("Enter comma-separated numbers: ")
numbers = user_input.split(',')
numbers_list = list(numbers)
numbers_tuple = tuple(numbers)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)

def compute_net_amount(transactions):
    balance = 0
    for transaction in transactions:
        action, amount = transaction.split()
        amount = int(amount)
        if action == 'D':
            balance += amount
        elif action == 'W':
            balance -= amount
    return balance

# Example usage
print("Enter transactions (type 'END' to finish):")
transactions = []
while True:
    transaction = input()
    if transaction == 'END':
        break
    transactions.append(transaction)

net_amount = compute_net_amount(transactions)
print("Net amount:", net_amount)
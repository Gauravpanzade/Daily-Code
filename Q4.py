# Write a program that takes a 3-digit number from the user and calculates the sum of its digits.

# Example:
# Input:  123
# Output: 6


# num = input("Enter a 3-digit number: ")

# sum_digits = int(num[0]) + int(num[1]) + int(num[2])

# print("Sum of digits:", sum_digits)




num = int(input("Enter a 3-digit number: "))

digit1 = num % 10
num = num // 10

digit2 = num % 10
num = num // 10

digit3 = num % 10

sum_digits = digit1 + digit2 + digit3

print("Sum of digits:", sum_digits)


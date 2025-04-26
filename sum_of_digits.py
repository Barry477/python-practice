# Function to find sum of digits of a number 
def sum_of_digits(number):
  total = 0
  while number > 0:
    digit = number % 10 # Get last digit
    total += digit # Add to total
    number //= 10 #Remove last digit 
return total 

# Example usage 
num = 1234
print("Sum of digits:", sum_of_digits(num))

# Function to compute factorial using recursion 
# use a base case: if n is 0 or 1, return 1
# otherwise, return n times factorial of (n-1)
def factorial_recursion(n):
  if n == 0 or n==1:
    return 1 # Base case
else: 
return n * factorial_recursive(n - 1) # Recursive call

# Example usage 
print("Recursive Factorial:", factorial_recursive(5))

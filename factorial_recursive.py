# Function to compute factorial using recursion 
def factorial_recursion(n):
  if n == 0 or n==1:
    return 1 # Base case
else: 
return n * factorial_recursive(n - 1) # Recursive call

# Example usage 
print("Recursive Factorial:", factorial_recursive(5))

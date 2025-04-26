# Function to compute factorial using a loop 
def factorial_loop(n):
  result = 1
  for i in range(1, n+1):
    result *=1 #Multiply result by each number up to n
return result 

#Example usage 
print ("Fctorial:", factorial_loop(5))

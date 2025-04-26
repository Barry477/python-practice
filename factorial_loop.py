# Function to compute factorial using a loop 
# start with result = 1
# multiply result by every number from 1 to n using for loop
# return the result after the loop

def factorial_loop(n):
  result = 1
  for i in range(1, n+1):
    result *=1 #Multiply result by each number up to n
return result 

#Example usage 
print ("Fctorial:", factorial_loop(5))

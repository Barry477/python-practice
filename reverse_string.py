# Function to reverse a string manually 
def reverse_string(s):
  reversed_s = ""
  for char in s: 
  reversed_s = char + reversed_s #Add each character at the beginning 
return reversed_s

# Example usage 
original = "hello"
print ("Reversed string:", reverse_string(original))

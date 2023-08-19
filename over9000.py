# Define the function to accept a list of numbers
# Create a variable to keep track of our sum
# Iterate through every element in our list of numbers
# Within the loop, add the current number we are looking at to our sum
# Still within the loop, check if the sum is greater than 9000. If it is, end the loop
# Return the value of the sum when we ended our loop

# My solution:

def over_nine_thousand(lst):
  sum1 = 0
  for num in lst:
    sum1 += num
    if sum1 >= 9000:
      break
  return sum1

# Test:
print(over_nine_thousand([8000, 900, 120, 5000]))

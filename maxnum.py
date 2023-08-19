# Define the function to accept a list of numbers called nums
# Set our default maximum value to be the first element in the list
# Loop through every number in the list of numbers
# Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
# Return the maximum number

# My solution:
def max_num(nums):
  maxnum = nums[0]
  for num in nums:
    if num > maxnum:
      maxnum = num
  return maxnum

# Test
print(max_num([50, -10, 0, 75, 20]))

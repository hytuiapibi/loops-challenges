# Define our function to accept two lists of numbers
# Create a new list to store our matching indices
# Loop through each index to the end of either of our lists
# Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
# Return our list of indices

# My solution:

def same_values(lst1, lst2):
  newlist = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      newlist.append(index)
  return newlist

# Test
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

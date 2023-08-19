# Define a function that has two input parameters for our lists
# Loop through every index in one of the lists from beginning to end
# Within the loop, compare the element in the first list at the current index against the element at the second list’s last index minus the current index. If there was a mismatch, then the lists aren’t reversed and we can return False
# If the loop ended successfully, then we know the lists are reversed and we can return True.


# My solution

def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True 


# Test
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

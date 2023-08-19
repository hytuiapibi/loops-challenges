#Define the function to accept two input parameters: lst1 and lst2
#Create two variables to record the two sums
#Loop through the first list and add up all of the numbers
#Loop through the second list and add up all of the numbers
#Compare the first and second sum and return the list with the greater sum

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num in lst1:
    sum1 += num
  for num2 in lst2:
    sum2 += num2
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

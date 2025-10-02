# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

#Importing Counter from collections to count frequency of elements
from collections import Counter
#defining the function to find the most frequent element
def most_frequent(numbers):
    #check for empty list and non-integer values
    if not numbers:
        raise TypeError("List must not be empty")
    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("List must contain only integers")
    #initialize counter and find most common element
    counter = Counter(numbers)
    most_common, _ = counter.most_common(1)[0]
    return most_common
  


"""
Time and Space Analysis for problem 1:
- Best-case: input list is empty or has one element and takes less steps to process
- Worst-case: input list has all unique elements and takes more steps to process
- Average-case: imput list has a mix of duplicates and unique elements
- Space complexity: O(n) for storing counts in the counter
- Why this approach? Using Counter simplifies counting and finding the most common element
- Could it be optimized? I coulkd do a better job handling edge cases with if statements
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    #check for empty list and non-list input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    #initialize set and result list
    seen = set()
    result = []
    #iterate through nums and add to result if not seen
    for x in nums:
        if x not in seen:
            # add to seen set and result list
            seen.add(x)
            # remove duplicates by adding only unseen elements to result
            result.append(x)
    # return the result list without duplicates
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: input list is empty or has all unique elements
- Worst-case:  input list has all duplicates and takes more steps to process
- Average-case: input list has a mix of duplicates and unique elements
- Space complexity:  There is O(n) space complexity for the seen set and result list
- Why this approach? Using a set for O(1) lookups to check for duplicates
- Could it be optimized? I could use a santity check for non-list inputs
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    # Check for a valid list imput
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    # Initialize sets for seen numbers and pairs
    seen = set()
    pairs = set()
    # Iterate through numbers to find pairs
    for num in nums:
        complement = target - num
    # If complement is in seen, add the pair to pairs set
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    # Return the list of unique pairs
    return list(pairs)


"""
Time and Space Analysis for problem 3:
- Best-case: input list is empty or has no valid pairs
- Worst-case: input list has many elements and many valid pairs 
- Average-case: input list has a mix of elements with some valid pairs
- Space complexity: O(n) for storing seen numbers and pairs 
- Why this approach? Using sets for O(1) lookups and to avoid duplicate pairs
- Could it be optimized?  I could use else statements to handle edge cases better
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    capacity = 1
    size = 0
    lst = [None] * capacity
    for i in range(n):
        if size == capacity:
            # Simulate resizing by doubling capacity
            print(f"Resizing from {capacity} to {capacity * 2}")
            # Double the capacity
            capacity *= 2
            # Create a new list and copy elements
            new_lst = [None] * capacity
            # Copy elements to new list
            for j in range(size):
                new_lst[j] = lst[j]
            lst = new_lst
       # Add the new item     
        lst[size] = i  
        size += 1
    return lst[:size] 

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the current size equals capacity
- What is the worst-case for a single append? O(n) when resizing occurs
- What is the amortized time per append overall? O(1) amortized time per append
- Space complexity: O(n) for the list storage
- Why does doubling reduce the cost overall? Doubling reduces the frequency of resizes, spreading the cost over many appends
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    # Check for valid list input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    # Initialize total and result list
    total = 0
    result = []
    # Iterate through nums to compute running total
    for num in nums:
        total += num
        # Append the current total to the result list
        result.append(total)
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: input list is empty or has one element
- Worst-case: input list has many elements
- Average-case: input list has a moderate number of elements
- Space complexity: O(n) for the result list
- Why this approach? Simple iteration and accumulation
- Could it be optimized? I Could add input validation for non-list inputs
"""

"""
The main aproach: 
1. We can't use any extra space.

2. We can use two pointers, one to iterate through the array and another to keep track of the position of the next non-val element.

3. We iterate through the array, and whenever we find an element that is not equal to val, we copy it to the position indicated by the second pointer(k) and increment that pointer.

4. Finally, the second pointer will indicate the new length of the array after removing all instances of val.
"""
nums = [3,2,2,3]
val = 3
k = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1
print(k)  # Output: 2




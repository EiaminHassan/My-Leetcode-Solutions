nums = [1,1,1,2,3]
k=0

for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        k+=1
        nums[k] = nums[i+1]

print(k+1)


nums = [2, 5, 3, 7, 3, 8]
target = 12
if target == 0 and nums.count(0) < 2:
    print(None)
    quit()

for i in range(len(nums)):
    x = target - nums[i]
    if x in nums:
        nums[i] = "None"
        print(nums.index(nums[i]), nums.index(x))
        break
else:
    print(None)





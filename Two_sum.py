
nums = [2, 5, 3, 7, 3, 8]
target = 12

d = []

for index, num in enumerate(nums):
    x = target - num
    h = num
    if x in nums and index != nums.index(x):
        d.append([index, nums.index(x)])
        break
if d:
    print(*sorted(d[0]))
else:
    print("None")

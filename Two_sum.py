
nums = [2, 5, 3, 7, 3, 8]
target = 1
d = []
if len(nums) > 1:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                d.append([i, j])
    if d:
        print(*d[0])
    else:
        print(None)
else:
    print(None)

# O(n^2)

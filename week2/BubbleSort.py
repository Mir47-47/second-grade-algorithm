n = int(input())

nums = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(1,n-i):
        if nums[j-1] > nums[j]:
            tempNum = nums[j-1]
            nums[j-1] = nums[j]
            nums[j] = tempNum
            count+=1


print(count)
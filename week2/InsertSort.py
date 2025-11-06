n = int(input())

nums = list(map(int, input().split()))

count = 0

for i in range(1,n):
    tempNum = nums[i]
    j = i-1
    while(j >= 0 and nums[j] > tempNum):
        nums[j+1] = nums[j]
        j -= 1
        count+=1
    nums[j+1] = tempNum
    count+=1


print(count)
print(nums)
n = int(input())

nums = list(map(int, input().split()))

count = 0

for i in range(n):
    maxNum = 0
    for j in range(1,n-i):
        if nums[maxNum] <= nums[j]:
            count+=1
            maxNum = j

    tempNum = nums[maxNum]
    nums[maxNum] = nums[n-1-i]
    nums[n-1-i] = tempNum


print(count)

def RaidxSort(arr, n, k):
    cnt = [0]*10
    arr2 = [0]*n
    for digit in range(1, k+1):
        for d in range(10):
            cnt[d]=0
        for i in range(n):
            cnt[arr[i]//(10**(digit-1))%10]+=1
            # print(arr[i]//(10**(digit-1))%10)
        start = [0]*10
        for d in range(1,10):
            start[d] = start[d-1] + cnt[d-1]
        # print(start)
        for i in range(n):
            # print(start[arr[i]//(10**(digit-1))%10])
            arr2[start[arr[i]//(10**(digit-1))%10]] = arr[i]
            start[arr[i]//(10**(digit-1))%10]+=1

        for i in range(n):
            arr[i] = arr2[i]
    return arr

n = list(map(int, input().split()))

nums = list(map(int, input().split()))

nums = RaidxSort(nums, n[0], n[1])

for i in range(n[0]):
    print(nums[i], end=' ')
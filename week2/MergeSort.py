n = int(input())

nums = list(map(int, input().split()))

def mergeSort(nums : list, p, r):
    count = 0
    if p < r:
        q = (p + r) // 2
        count += mergeSort(nums, p, q)
        count += mergeSort(nums, q + 1, r)
        count += merge(nums, p, q, r)
    return count

def merge(nums:list, p, q, r):
    count = 0
    tem = []
    i = p
    j = q + 1
    t = 1
    while(i<=q and j<=r):
        count += 1
        if nums[i] < nums[j]:
            tem.append(nums[i])
            t+=1
            i+=1
        else:
            tem.append(nums[j])
            t+=1
            j+=1

    while(i<=q):
        tem.append(nums[i])
        i+=1
        t+=1
    while(j<=r):
        tem.append(nums[j])
        j+=1
        t+=1

    i=p
    t=1
    while(i<=r):
        nums[i] = tem[t-1]
        i+=1
        t+=1
    return count


print(mergeSort(nums, 0, n-1))
print(nums)
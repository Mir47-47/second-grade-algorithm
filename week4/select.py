def select(arr, p, r, i):
    if(p == r):
        return arr[p]
    q = partition(arr, p, r);
    k = q - p + 1
    if(i < k):
        return select(arr, p, q-1, i)
    elif(i > k):
        return select(arr, q+1, r, i-k)
    else:
        return arr[q]

def partition(arr, p, r):
    global cnt
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if(arr[j] <= x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            cnt+=1
    arr[i+1], arr[r] = arr[r], arr[i+1]
    cnt+=1
    return i+1





n = list(map(int, input().split()))
nums = list(map(int, input().split()))

cnt = 0

select(nums, 0, n[0]-1, n[1])
print(cnt)
global count

def partition(arr, p, r):
    global count
    x=arr[r]
    i=p-1
    for j in range(p, r):
        if arr[j] < x:
            temp = arr[i+1]
            i+=1
            arr[i] = arr[j]
            arr[j] = temp
            count+=1

    temp = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = temp
    count+=1
    return i+1


def quickSrot(arr, p, r):
    if(p<r):

        q = partition(arr, p, r)
        quickSrot(arr, p, q-1)
        quickSrot(arr, q+1, r)
    return arr




n = int(input())
arr = list(map(int, input().split()))
count=0
quickSrot(arr, 0, n-1)
print(count)
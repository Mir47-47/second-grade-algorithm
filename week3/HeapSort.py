

def heapSort(arr, n):
    global count
    buildHeap(arr, n)
    for i in range(n-1, 0, -1):
        arr[i] = deleteMax(arr, i+1)
def buildHeap(arr, n):
    global count
    for i in range(int((n-2)/2), -1, -1):
        percolateDown(arr, i, n)
    count = 0

def percolateDown(arr, k, n):
    global count
    child = 2*k+1
    right = 2*k+2
    if(child <= n-1):
        if(right<=n-1 and arr[child] <= arr[right]):
            child = right
        if(arr[k] < arr[child]):
            temp = arr[k]
            arr[k] = arr[child]
            arr[child] = temp
            count += 1
            percolateDown(arr, child, n)


def deleteMax(arr, n):
    max = arr[0]
    arr[0] = arr[n-1]
    n-=1
    percolateDown(arr, 0, n)
    return max


n = int(input())
arr = list(map(int, input().split()))

count = 0
heapSort(arr, n)
print(arr)
print(count)
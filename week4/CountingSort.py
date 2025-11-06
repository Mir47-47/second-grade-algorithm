def countingSort(A, B, n):
    k = max(A)-min(A)+1
    C = [0]*k
    for i in range(n):
        C[A[i]-min(A)]+=1
    for i in range(1, k):
        C[i] = C[i]+C[i-1]
    for i in range(k):
        print(C[i], end=' ')
    for j in range(n-1, 1, -1):
        B[C[A[j]-min(A)]-1] = A[j]
        C[A[j]-min(A)]-=1





n = int(input())

nums = list(map(int, input().split()))

B = [0]*n

countingSort(nums, B, n)
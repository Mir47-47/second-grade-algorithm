from math import ceil


def linear_select(A, p, r, i) :
    if(r - p + 1 <= 5) :
        return select(A, p, r, i)
    nums_5 = list()
    nums_5_n = r+1-p
    for h in range((nums_5_n//5)):
        nums_5.append(A[h*5:(h*5)+5])


    if(nums_5_n%5 != 0):
        nums_5.append(A[(len(A)//5)*5:len(A)])

    medians = list()
    for k in range(p, r + 1, 5):
        end = min(k + 4, r)

        group_size = end - k + 1

        median_rank = (group_size + 1) // 2

        median_value = select(A, k, end, median_rank)
        medians.append(median_value)


    M = linear_select(medians, 0, len(medians) - 1, ceil(len(medians)/2))

    q = partitionByMedian(A, p, r, M)
    print(M)
    k = q - p + 1

    if i < k:
        return linear_select(A, p, q - 1, i)

    elif i > k:
        return linear_select(A, q + 1, r, i - k)

    else: # i == k
        return A[q]

def partitionByMedian(A, p, r, M) :
    current_arr = A[p:r+1]
    i = A.index(M)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def select(arr, p, r, i):
    if(p == r):
        return arr[p]
    q = partition(arr, p, r)
    k = q - p + 1
    if i < k and r>p:
        return select(arr, p, q-1, i)
    elif i > k and r>p:
        return select(arr, q+1, r, i-k)
    else:
        return arr[q]


def partition(A, p, r) :
    x = A[r]
    i = p - 1
    for j in range(p , r) :
        if(A[j] <= x) :
            i+=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


n = list(map(int, input().split()))
nums = list(map(int, input().split()))

linear_select(nums, 0, n[0]-1, n[1])
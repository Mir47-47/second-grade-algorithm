def fib2(n, f, count) :
    if n == 0 :
        return f[n], 0
    if f[n] == 0:
        if n == 1 or n == 2:
            f[n] = 1
        else:
            if f[n-1] == 0:
                f[n-1], t= fib2(n-1, f, count)
                count+=t
            if f[n-2] == 0:
                f[n-2], t= fib2(n-2, f, count)
                count+=t
            f[n] = f[n-1] + f[n-2]
            count+=1
    else :
        count+=1
    return f[n], count

n = int(input())
f = [0] * (n + 1)
count = 0
t,c=fib2(n, f, count)
print(c)
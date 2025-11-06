
def HashKey(key, table_size):
    hash_value = key%table_size
    return hash_value

def HashInsert(hash_table, key):
    count = 0
    table_size = len(hash_table)
    hash_value = HashKey(key, table_size)
    if hash_table[hash_value] is None:
        hash_table[hash_value] = key
    else:
        initial_value = hash_table[hash_value]
        while True:
            count += 1
            hash_value = (hash_value + 1) % table_size
            if hash_value == initial_value:
                break
            if hash_table[hash_value] is None:
                hash_table[hash_value] = key
                break
    return count


N = int(input())
numbers = list(map(int, input().split()))

M = 2*N

while True:
    is_prime = True
    for i in range(M-1, 1, -1):
        if M % i == 0:
            is_prime = False
            break
    if is_prime:
        break
    M += 1

hash_table = [None] * M

count = 0

for number in numbers:
    count+=HashInsert(hash_table, number)

print(count)
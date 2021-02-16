

def numberOfOnes(n: int) -> bool:
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count


print(numberOfOnes(64))
print(numberOfOnes(99))

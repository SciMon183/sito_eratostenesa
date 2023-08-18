
def is_prime(n):
    if 1>=n:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

print(is_prime(2))

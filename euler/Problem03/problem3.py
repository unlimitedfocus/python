# python
def prime_divisors(n):
    result = []
    i = 2
    while i <= n:
        if n % i == 0:
            result.append(i)
            n /= i
        i += 1
    return result

def largest_prime(n):
    return prime_divisors(n)[-1]

print largest_prime(600851475143)

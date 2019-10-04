p = int(input('enter a prime number '))
q = int(input('enter another prime number '))

def is_prime(n: int) -> bool:     #проверка на простое число
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                return False
            else:
                return True
    else:
        return False

if (is_prime(p)==False) or (is_prime(q)==False):
    raise ValueError('both must be prime')
elif p==q:
    raise ValueError('cannot be equal')

def gcd(a: int, b: int) -> int: #алгоритм евклида
        while b != 0:
            (a, b) = (b, a % b)
        return a

def generate_keypair():
    n = p*q
    phi = (p - 1)*(q - 1)
    import random
    e = random.randrange(1, phi)
    while not ((is_prime(e)==True) and (gcd(e, phi)==1)):
        e = random.randrange(1, phi)
    d = random.randrange(1, phi)
    while not ((d * e % phi == 1) and e != d):
        d = random.randrange(1, phi)
    return (e, n), (d, n)


print(generate_keypair())
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
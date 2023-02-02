def s12(n):
    new = ''
    while n:
        new = str(n % 12) + new
        n //= 12
    return n


print(s12(5))
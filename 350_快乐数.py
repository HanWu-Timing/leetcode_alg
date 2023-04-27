def ishappy(n):
    result = set()
    while n != 1 and n not in result:
        result.add(n)
        n = get_next(n)
        print(n, " ")
    return n == 1

def get_next(n):
    sum = 0
    while n > 0:
        sum += (n % 10) ** 2
        n //= 10
    return sum

n = int(input())
ishappy(n)
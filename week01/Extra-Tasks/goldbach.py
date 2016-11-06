def getKey(item):
        return item[0]


def goldbach(n):
    primes = list(n for n in range(2, n) if all(n % d for d in range(2, n)))
    result = []

    for prime in primes:
        for p in primes:
            if prime + p == n:
                result.append((prime, p))

    result = list(set(tuple(sorted(result[i])) for i in range(len(result))))

    return sorted(result, key=getKey)


print(goldbach(10))

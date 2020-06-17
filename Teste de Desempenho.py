import time


def infinite_prime():
    number = 1
    while True:
        if verify_prime(number) == True:
            yield number
        if number > 10000:
            break
        number += 1


def verify_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    root = int(num ** 0.5)
    for count in range(root, 1, -1):
        if num % count == 0:
            return False
    return True


def verify_prime_noroot(num):
    for count in range(2, number + 1, 1):
        if num % count == 0:
            return False
    return True


def infinite_prime2():
    number = 1
    while True:
        if verify_prime_noroot(number) == True:
            yield number
        if number > 10000:
            break
        number += 1


t1 = time.time()
for number in infinite_prime():
    print(number)
t2 = time.time()
print(f'Duração do algoritmo: {t2 - t1} segundos')

for count in range(5):
    print(count, end="...", flush=True)
    time.sleep(1)

t1 = time.time()
for number in infinite_prime2():
    print(number)
t2 = time.time()
print(f'Duração do algoritmo: {t2 - t1} segundos')

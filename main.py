#!/usr/bin/python3

import math
import multiprocessing
from sys import argv


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            amount += 1
    return amount


def step1(n):
    for b in range(2, math.floor(math.log2(n) + 1)):
        a = n ** (1 / b)
        if a.is_integer():
            return False
    return True


def step2(n):
    mk = math.floor(math.log2(n) ** 2)
    nexr = True
    r = 1
    while nexr:
        r += 1
        nexr = False
        k = 0
        while k <= mk and not nexr:
            k = k + 1
            if pow(n, k, r) in (0, 1):
                nexr = True
    return r


def step3(n, r):
    for a in range(1, r + 1):
        if 1 < math.gcd(a, n) < n:
            return False
    return True


def step4(n, r):
    if n <= r:
        print(f"{n} - prime. Step 4")
        return True
    return False


def step5(n, r):
    max = math.sqrt(phi(r))
    rn = math.floor(max * math.log2(n))
    if rn > n:
        rn = n
    threads = []
    ran = rn / 8
    ran = math.floor(ran)
    if ran == 0:
        ran = 1

    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    for a in range(0, rn, ran):
        process = multiprocessing.Process(
            target=step5_check, args=(n, a, a + ran, return_dict)
        )
        process.start()
        threads.append(process)
    for i in threads:
        i.join()

    if False not in return_dict.values():
        print(f"{n} - prime. Step 5")
        return True
    return False


def step5_check(n, bot, top, return_dict):
    x = bot / (top - bot)
    if bot == 0:
        bot = 1
    for a in range(bot, top):
        b = pow(a, n, n)
        if b - a != 0:
            return_dict[x] = False
            return False
    return_dict[x] = True
    return True


def aks(n):
    if step1(n):
        r = step2(n)
        return step3(n, r) and (step4(n, r) or step5(n, r))
    return False


def trivial(n):
    if n == 2:
        return True
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    for i in range(int(argv[1]), int(argv[2])):
        assert aks(i) == trivial(i)


if __name__ == "__main__":
    main()

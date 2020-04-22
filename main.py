#!/usr/bin/python3

import math
import multiprocessing


def exp_func(x, y, m):
    exp = bin(y)
    value = x
    for i in range(3, len(exp)):
        value = value * value % m
        if exp[i:i + 1] == '1':
            value = value * x % m
    return value


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            amount += 1
    return amount


def step1(n):
    for b in range(2, int(math.log2(n) + 1)):
        a = n ** (1 / b)
        if math.floor(a) == a:
            return False
    return True


def step2(n):
    mk = math.floor(math.log2(n) ** 2)
    nexr = True
    r = 1
    while nexr is True:
        r += 1
        nexr = False
        k = 0
        while k <= mk and nexr is False:
            k = k + 1
            if exp_func(n, k, r) in (0, 1):
                nexr = True
    return r


def step3(n, r):
    for a in range(1, r + 1):
        if (1 < math.gcd(a, n)) and (math.gcd(a, n) < n):
            return False


def step4(n, r):
    if n <= r:
        print("[+]" + str(n) + " is a Prime Step 4")
        return True
    else:
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
        process = multiprocessing.Process(target=step5_check, args=(n, a, a + ran, return_dict))
        process.start()
        threads.append(process)
    for i in threads:
        i.join()

    if False not in return_dict.values():
        print("[+]" + str(n) + " is a Prime Number Step 5")
        return True
    else:
        return False


def step5_check(n, unten, oben, return_dict):
    x = unten / (oben - unten)
    if unten == 0:
        unten = 1
    for a in range(unten, oben):
        b = exp_func(a, n, n)
        if b - a != 0:
            return_dict[x] = False
            return False

    return_dict[x] = True
    return True


def aks(n):
    if step1(n) is True:
        r = step2(n)
        if step3(n, r) is not False:
            if step4(n, r) is not True:
                if True is not step5(n, r):
                    return False
                else:
                    return True
            else:
                return True
        else:
            return False
    else:
        return False


def trivial(n):
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True


def main():
    for i in range(2, 300):
        assert aks(i) == trivial(i)


if __name__ == '__main__':
    main()

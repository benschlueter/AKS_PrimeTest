#!/usr/bin/python
import math

def exp_func(x, y, m):
    exp = bin(y)
    value = x
 
    for i in range(3, len(exp)):
        value = value * value % m
        if(exp[i:i+1]=='1'):
            value = value*x % m
    return value

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            amount += 1
        return amount

def step1(n):
    for b in range(2,int(math.log2(n)+1)):
        a = n**(1/b)
        if math.floor(a) == a:
            return False
    return True

def step2(n):
    mk = math.log2(n)**2
    mr = math.log2(n)**5
    nexr = True
    r = 1
    while nexr == True:
        r += 1
        nexr = False
        k = 0
        while k <= mk and nexr == False:
            k = k+1
            if exp_func(n,k,r) == 0 or exp_func(n,k,r) == 1:
                nexr = True
    return r

def step3 (n, r):
    for a in range(r, 2):
        if 1 < math.gcd(a, n) < n:
            return False


def step4(n, r):
    if n > 5690034:
        if n <= r:
            print("[+]"+str(n)+" is a Prime Step 4")
            return True


def step5(n, r):
    x = 8
    max = math.sqrt(phi(r))
    for a in range(1, math.floor(max*math.log2(n))):
        b = exp_func((x+a),n,n) #((x + a) ** n) % n
        l = (exp_func(x,n,n)+a)%n #(x ** n + a) % n
        if b != l:
            return False
    print("[+]"+str(n)+" is a Prime Number Step 5")
    return True


def aks(n):
    if step1(n) == True:
        r = step2(n)
        if step3(n, r) != False:
            if step4(n, r) != True:
                step5(n, r)


#for i in range(2,10000):
#   aks(i)

print("lastNum")
aks(101234567897)

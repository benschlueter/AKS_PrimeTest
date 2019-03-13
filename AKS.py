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
            #print("[-]"+str(n)+" is no Prime 1")
            return False
    return True

def step2(n):
    mk = math.log2(n)**2
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
    for a in range(1,r+1):
        if ((1 < math.gcd(a, n)) and (math.gcd(a,n) < n)):
            #print("[-]"+str(n)+" is no Prime 3")
            return False

def step4(n, r):
    if n > 5690034:
        if n <= r:
            print("[+]"+str(n)+" is a Prime Step 4")
            return True


def step5(n, r):
    x = 7
    max = math.sqrt(phi(r))
    rn = math.floor(max*math.log2(n))
    cache = exp_func(x,n,n)
    for a in range(1, rn+1):
        b = exp_func((x+a),n,n) #((x + a) ** n) % n
        l = (cache+a)%n #(x ** n + a) % n
        if b != l:
            #print("[-]"+str(n)+" is no Prime 5")
            return False
    print("[+]"+str(n)+" is a Prime Number Step 5")
    return True


def aks(n):
    #print("Testing Number: "+str(n))
    if step1(n) == True:
        r = step2(n)
        if step3(n, r) != False:
            if step4(n, r) != True:
                step5(n, r)



for i in range(2,1000):
   aks(i)
#print(100207100213100237100267*100207100213100237100267)
#aks(671998030559713968361666935769)

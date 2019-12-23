#!/usr/bin/python
import math
import multiprocessing


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
    mk = math.floor(math.log2(n)**2)
    nexr = True
    r = 1
    while nexr == True:
        r += 1
        nexr = False
        k = 0
        while k <= mk and nexr == False:
            k = k+1
            if exp_func(n,k,r) in (0,1):
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
    max = math.sqrt(phi(r))
    rn = math.floor(max*math.log2(n))
    if rn > n :
        rn = n
    threads = []
    ran = rn/8
    #print("rn:",rn)
    ran = math.floor(ran)
    if ran==0:
        ran = 1 
    for a in range(0,rn,ran):
        process = multiprocessing.Process(target=step5_check,args=(n,a,a+ran))
        process.start()
        threads.append(process)
    for i in threads:
        i.join()

    print("[+]"+str(n)+" is a Prime Number Step 5")
    return True

def step5_check(n,unten,oben):
    if unten == 0:
        unten = 1
    for a in range(unten,oben):
        b = exp_func(a,n,n) #((x + a) ** n) % n
        #print(b)
        if b - a != 0:
            #print("[-]"+str(n)+" is no Prime 5")
            return False

    return True

def aks(n):
    #print("Testing Number: "+str(n))
    #print("step 1:")
    if step1(n) == True:
        #print("step 2:")
        r = step2(n)
        #print("step 3:")
        if step3(n, r) != False:
            #print("step 4:")
            if step4(n, r) != True:
                step5(n, r)



#for i in range(2,100):
#   aks(i)
#aks(11)
#print(100207100213100237100267*100207100213100237100267)
aks(671998030559713968361666935769)

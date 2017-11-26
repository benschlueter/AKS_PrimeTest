#!/usr/bin/python
import math

def phi(n):
   amount = 0

   for k in range(1, n + 1):
       if math.gcd(k,n) == 1:
           amount += 1
   return amount

def step1(n):
   for b in range(2,int(math.log2(n)+1)):
       a = n**(1/b)
       if math.floor(a) == a:  #Integer Prüfen
           #print("[-] "+str(n)+" No Prime Number Step 1")    #Hat eine Wurzel falls es ein Int ist
           return False
   return True

def step2(n):
   mk = math.log2(n)**2   #MaximalWerte
   mr = math.log2(n)**5   #MaximalWerte
   nexr = True
   r = 1
   while nexr == True:
       r +=1
       nexr = False
       k = 0
       while k <= mk and nexr == False:
           k = k+1
           if (n**k) % r == 0 or (n**k) % r == 1:
               nexr = True
   return r

def step3 (n,r):
   for a in range(r,2): #Alle Zaheln von r bis 2 durchgehen
       if 1 < math.gcd(a,n) < n:       #
           #print("[-]"+str(n)+" No Prime Number Step 3")
           return False

def step4(n,r):
   if n > 5690034: #gilt nur für Zahlen bis .....
       if n <= r: #Wenn r größer als n ist n eine Primzahl
           print("[+]"+str(n)+" is a Prime Step 4")
           return True

def step5(n,r):
   x = 8
   max = math.sqrt(phi(r))
   for a in range(1,math.floor(max*math.log2(n))):
       b = ((x + a) ** n) % n
       l = (x ** n + a) % n
       if b != l:
           #print("[-] " + str(n) + " No Prime Number Step 5")
           return False
   print("[+]"+str(n)+" is a Prime Number Step 5")
   return True

for n in range(2,10000000):
   if step1(n) == True:
       r = step2(n)
       if step3(n,r) != False:
           if step4(n,r) != True:
               step5(n,r)

 

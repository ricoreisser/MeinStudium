from math import pow,sqrt

def num(s):
    try:
        return float(s)
    except ValueError:
        return False
a=False
while(a==False):
    a=num(input('a eingeben:'))
b=False
while(b==False):
    b=num(input('b eingeben:'))
c=False
while(c==False):
    c=num(input('c eingeben:'))
res=0.5*sqrt((2*(pow(b,2)+pow(c,2)))-pow(a,2))
print('die Seitenhalbierende von a ist:',+res) 

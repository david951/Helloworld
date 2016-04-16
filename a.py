a=(int(raw_input("n= ")))
esprimo = True
n=2
while(n<a):
    if(a%n==0):
        esprimo = False
    n = n+1 

if(esprimo == True):
    print "Es primo"
else:
    print "No es primo"

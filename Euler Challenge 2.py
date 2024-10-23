#code

Values = [2]
fibo1 = 1
fibo2 = 2

fibo3 = 3

while fibo2 <= 4000000:
    fibo3 = fibo1+fibo2
    Check = fibo3%2
    if Check == 0:
        Values.append(fibo3)
    fibo1=fibo2
    fibo2=fibo3
    

Repeat = len(Values)
Sum = 0
for i in range(Repeat):
    Sum = Sum+Values[i]
    
print Sum
print 4613732
    


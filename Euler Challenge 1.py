#code

Values = []


for i in range(1000):
    Check = i%3
    if Check == 0:
        Values.append(i)
    Check = i%5
    if Check == 0:
        if not i in Values:
            Values.append(i)

Repeat = len(Values)
Sum = 0
for i in range(Repeat):
    Sum = Sum+Values[i]
print Sum
print 233168
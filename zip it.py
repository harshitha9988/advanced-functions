s1={2,3,1}
s2={'b','a','c'}
s3=list(zip(s1,s2))
print(s3,"\n")

l1=[10,20,30,40]
l2=[100,200,300,400]
for x, y in zip(l1,l2[::-1]):
    print(x,y)

s=['reliance','infosys','tcs']
p=[2175,1127,2750]

nd={s: p for s,
        p in zip(s,p)}
print('\n{}'.format(nd))
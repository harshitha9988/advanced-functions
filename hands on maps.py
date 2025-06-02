n1=[1,2,3]
n2=[4,5,6]
r=map(lambda x, y: x+y, n1, n2)
print("Addition of two list")
print(list(r))


a=[1,2,3,4,5]
def sq(n):
    return n*n
s=list(map(sq, a))
print("Square of numbers in list")
print(s)
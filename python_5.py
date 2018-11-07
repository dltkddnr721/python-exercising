a= int(input())
if a % 10 <=5:
    b=a//10
    c=b//5 + 1
    print(b)
    print(c)
    print(b*8+c*5+a)
else :
    b=a//10 +1
    c=0
    print(b)
    print(c)
    print(b*8+a)
    

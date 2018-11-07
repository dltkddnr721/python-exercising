a=1
b=1
while a !=0:
    a=int(input())
    if a == 0:
        break
    b=int(input())
    if (a*b)%6==0:
        print('all')
    elif (a*b)%3==0:
        print('three')
    elif (a*b)%2==0:
        print('two')
    else:
        print("none")

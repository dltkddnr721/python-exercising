i=[]
sum1 = 0
while sum1<300:
    b=int(input())
    sum1+=b
    i.append(b)
    if 17 in i:
        print("정답입니다")
        break
    else :
        print("남은수",300-sum1,"만큼의 숫자를 더 적을 수 있습니다")
print(sum1,i)

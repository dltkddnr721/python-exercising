bio = ['0번','1번','2번']
bio.append("3번")
bio.insert(4,"4번")
for a in bio:
    print(a+'을 뽑았습니다.')
for value in range(1,99,10):
    print(value)
square=[]
for b in range(1,11,1):
    c=b**2
    square.append(c)
print(square)
print(square[0:4])
car = ['bmw','benz','carnival','mou']
if car=='bmw':
    print(car+"is sold out")
car1 = "abc"
print("is car1 == 'abc'? I predict true.")
print (car1=='abc')

age = 19
if age>19:
    print("you are old")

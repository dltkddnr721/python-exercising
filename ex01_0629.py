layer1 = int(input())
layer2 = int(input())

num1 = layer1 & layer2
num2 = layer1 | layer2
result1 = 0
result2  = 0

result1 += int(num1 / 8)  
num1 %=8                      
result1 += int(num1 / 4)
num1 %=4
result1 += int(num1 /2)
num1 %=2
result1 += num1

result2 += int(num2 / 8)
num2 %=8
result2 += int(num2 / 4)
num2 %=4
result2 += int(num2 /2)
num2 %=2
result2 += num2

print(result1)
print(result2)

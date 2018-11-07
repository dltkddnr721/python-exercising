import random

print("프린트 가위 바위 보 게임")
#컴퓨터를 def로 지정해 놓고 random을 통해 1,3값중 아무것을 선택하게 한후 1을 난수로 택하면 가위 2를선택하면 바위 3을선택하면 보가 출력되도록함
def computer():
        com = random.randint(1,3)
        if (computer == 1):
                computer == "가위";
        elif (computer == 2):
                       computer == "바위";
        elif (computer == 3):
                       computer == "보";

#user가 숫자를 선택할수 있도록 raw_input을 사용 
user= int(raw_input("가위는 1 바위는 2 보는 3:"))
# user와 컴퓨터가 이기고 짐에따라 프린드를 하게 만드는관정if로 한값을 설정한다음 나머지는 elif로 만들었음
if (user == computer):
        print("비김")

elif (user == "바위"):
        if (computer == "보"):
            print("컴퓨터가 이김")

elif (user == "보"):
        if (computer == "바위"):
            print("플레이어가 이김")

elif (user == "보"):
        if (computer == "가위"):
            print("컴퓨터가 이김")

elif(user == "가위"):
    if (computer == "바위"):
        print("사용자 :가위 컴퓨터 : 바위 컴퓨터승)

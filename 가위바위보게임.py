import random

print("����Ʈ ���� ���� �� ����")
#��ǻ�͸� def�� ������ ���� random�� ���� 1,3���� �ƹ����� �����ϰ� ���� 1�� ������ ���ϸ� ���� 2�������ϸ� ���� 3�������ϸ� ���� ��µǵ�����
def computer():
        com = random.randint(1,3)
        if (computer == 1):
                computer == "����";
        elif (computer == 2):
                       computer == "����";
        elif (computer == 3):
                       computer == "��";

#user�� ���ڸ� �����Ҽ� �ֵ��� raw_input�� ��� 
user= int(raw_input("������ 1 ������ 2 ���� 3:"))
# user�� ��ǻ�Ͱ� �̱�� �������� �����带 �ϰ� ����°���if�� �Ѱ��� �����Ѵ��� �������� elif�� �������
if (user == computer):
        print("���")

elif (user == "����"):
        if (computer == "��"):
            print("��ǻ�Ͱ� �̱�")

elif (user == "��"):
        if (computer == "����"):
            print("�÷��̾ �̱�")

elif (user == "��"):
        if (computer == "����"):
            print("��ǻ�Ͱ� �̱�")

elif(user == "����"):
    if (computer == "����"):
        print("����� :���� ��ǻ�� : ���� ��ǻ�ͽ�)

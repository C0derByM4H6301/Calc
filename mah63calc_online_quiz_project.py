#Coded by https://github.com/C0derByM4H6301 for online exam
while True:
    first_num=input("First number: ")
    second_num=input("Second number: ")
    choice=input("Choose between +, -, *, / : ")
    if choice=="*":
        first_num=int(first_num)
        second_num=int(second_num)
        sonuc=first_num * second_num
        sonuc=int(sonuc)
        first_num=str(first_num)
        second_num=str(second_num)
        sonuc=str(sonuc)
        print(first_num+" * "+second_num+ "="+sonuc )

    if choice=="/":
        first_num=int(first_num)
        second_num=int(second_num)
        sonuc=first_num / second_num
        sonuc=int(sonuc)
        first_num=str(first_num)
        second_num=str(second_num)
        sonuc=str(sonuc)
        print(first_num+" / "+second_num+"="+sonuc)

    if choice=="+":
        first_num=int(first_num)
        second_num=int(second_num)
        sonuc=first_num * second_num
        sonuc=int(sonuc)
        first_num=str(first_num)
        second_num=str(second_num)
        sonuc=str(sonuc)
        print(first_num+" + "+second_num+"="+sonuc)

    if choice=="-":
        first_num=int(first_num)
        second_num=int(second_num)
        sonuc=first_num * second_num
        sonuc=int(sonuc)
        first_num=str(first_num)
        second_num=str(second_num)
        sonuc=str(sonuc)
        print(first_num+" - "+second_num+"="+sonuc)

    if choice!="+" and choice!="-" and choice!="*" and choice!="/":
        print("Please type: +, -, *, / ")
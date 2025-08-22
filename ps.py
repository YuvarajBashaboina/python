# #check wheather div by 3 and 5 
# while True:
#     print("1. addition  2. substration 3. multiplication 4.division 5.Another option will exit")
#     choice=input("enter the choice")
#     if choice == "1" or choice == "addition":
#         num1 = float(input("enter the num1 to addition :"))
#         num2 = float(input("enter the num2 to addition :"))
#         print(num1+num2)
#     elif choice == "2" or choice == "substration":
#         num1 = float(input("enter the num1 to substration :"))
#         num2 = float(input("enter the num2 to substration :"))
#         print(num1-num2)
#     elif choice == "3" or choice == " multiplication":
#         num1 = float(input("enter the num1 to multiplication :"))
#         num2 = float(input("enter the num2 to multiplication :"))
#         print(num1*num2)
#     elif choice == "4" or choice == "division":
#         num1 = float(input("enter the num1 to division :"))
#         num2 = float(input("enter the num2 to division :"))
#         if num2 != 0:
#             print(num1/num2)
#         else:
#             print("div by 0 not possible")
#     else:
#         print("not valid")
#         print("---exit---")
#         break
# #check wheather div by 3 and 5 
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i,end=" ")
#         print('Divisible by 3 and 5')  
# # factorial of a num
# num = int(input('enter the number'))
# fact = 1 
# for i in range(1,num+1):
#     fact *=i
# print("Factorial of a number",num,"is",fact)
# basic login system
correct_password = "union123"
count=1
while count <=3:
    password = input("enter the password:")
    if password == correct_password:
        print("login succesful")
        break
    elif password != correct_password:
        print("wrong password")
        count += 1
        if count > 3:
            print("exceeded your limits wait for 24hrs")
    else:
        print("something went wrong")
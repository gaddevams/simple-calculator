# importing all modules
import addition
import subraction
import multiplication
import division
import modulesDivision

operations=(
    "1.Addition\n"
    "2.Subration\n"
    "3.Multipliation\n"
    "4.Division\n"
    "5.Modules Division"
)


# main function
if __name__ == "__main__":
    print(*operations)
    choice=int(input("please select your operation(1-6):"))
    if choice==1:
        num1= int(input("EEnter number 1:"))
        num2= int(input("EEnter number 2:"))
        print(addition.add(a=num1,b=num2))
    elif choice==2:
        num1= int(input("EEnter number 1:"))
        num2= int(input("EEnter number 2:"))
        print(subraction.sub(a=num1,b=num2))
    elif choice==3:
        num1= int(input("EEnter number 1:"))
        num2= int(input("EEnter number 2:"))
        print(multiplication.mul(a=num1,b=num2))
    elif choice==4:
        num1= int(input("EEnter number 1:"))
        num2= int(input("EEnter number 2:"))
        print (division.div(a=num1,b=num2))
    elif choice==5:
        num1= int(input("EEnter number 1:"))
        num2= int(input("EEnter number 2:"))
        print(modulesDivision.modDiv(a=num1,b=num2))
    elif choice==6:
        print("Exit from calculator")
        exit()
    else:
        print("Please select the operation between 1-6")

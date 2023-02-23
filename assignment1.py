# 1 Program to divide two numbers

def divide(iNo1,iNo2):
    iAns = 0
    if(iNo2<=0):
        return -1
    iAns = iNo1/iNo2
    return iAns    


iValue1 = 15
iValue2 = 30
iRet = divide(iValue1,iValue2)
print("Division is ",iRet)

# 2 Program to print 5 times "Marvellous " on screen

def Display():
    for i in range(5):
        print("Marvellous")
Display()

# 3 Program to print 5 to 1 numbers on screen
def display():
    for i in range(5,0,-1):
        print(i)

display()

# 4 Accept one number and check whether is divisible by 5 or not
def Check(a):
    if((a%5)==0):
        return True
    else:
        return False

a = int(input("Enter a number to check it is divisible by 5 or not"))
b = Check(a)
if b == True:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")


# 5 Accept one number from user and print taht number of * on screen
def Accept(c):
    for i in range(c):
        print("*")
c = int(input("Enter number which you have to print that number of * on screen"))
Accept(c)

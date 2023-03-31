# Mihirs lab 1 part 2
print("___ ___  ____")

print("|   |   ||    \ ")

print("| _   _ ||  o  )")

print("|  \_/  ||   _/")

print("|   |   ||  |")

print("|   |   ||  |")
print("|___|___||__|")

def takeInput(**arg):
    A=int(input("Enter a number "))
    B=int(input("Enter second number "))
    sign_=str(input("Select an operator (/,*,-,+) "))
    return [A,B,sign_]

def displayResult(Ar,Br,sign_r):
    output=0
    if sign_r=="*":
        output=Ar*Br
    elif sign_r=="+":
        output=Ar+Br
    elif sign_r=="-":
        output=Ar-Br
    elif sign_r=="/":
        output=Ar/Br
    print(f"{Ar} {sign_r} {Br} = {output}")

list_=takeInput()
a=list_[0]
b=list_[1]
c=list_[2]
output2=displayResult(a,b,c)
#mihirs program
print("___ ___  ____")

print("|   |   ||    \ ")

print("| _   _ ||  o  )")

print("|  \_/  ||   _/")

print("|   |   ||  |")

print("|   |   ||  |")
print("|___|___||__|")

print("\n")
count=0
output=0
print(("Melanie Dental Clinic").center(100))
Patientname=input(("Enter patient's name: "))
Cleaning=input("Was cleaning performed? (y/n): ")
Cavity=input("Was cavity-filling performed? (y/n): ") 
x_ray=input("Was X-Ray performed? (y/n): ")
if Cleaning=="y":
    count+=60
if Cavity=="y":
    count+=200
if x_ray=="y":
    count+=100

if count>300:
    count=count-count*(0.10)
elif count>200:
    count=count-count*(0.5)
else:
    pass
output=count*0.15
print("\n")
print("Melanie Dental Clinic")
print(("-"*150).center(100))
print("Receipt for patient name: ",Patientname)
print("-"*150)
print(" Subtotal: ",count)
print("      Tax: ",output)
print("-"*150)
print("    total: ",count+output)


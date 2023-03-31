#mihirs program
def calculate_bill(cleaning, cavity_filling, x_ray):
    Bill = 0
    if cleaning == 'y':
        Bill += 60
    if cavity_filling == 'y':
         Bill += 200
    if x_ray == 'y':
         Bill += 100
    tax = Bill * 0.15
    Total = Bill + tax
    if  Total > 300:
         Total *= 0.9
    elif  Total > 200:
         Total *= 0.95
    return  Bill, Total ,tax

name = input("Enter patient's name: ")
cleaning = input("Was cleaning performed? (y/n): ")
cavity_filling = input("Was cavity-filling performed? (y/n): ")
x_ray = input("Was X-Ray performed? (y/n): ")

Bill,total,tax = calculate_bill(cleaning, cavity_filling, x_ray)

print("Melanie Dental Clinic")
print("Patient name:", name)
print("Cleaning:", cleaning)
print("Cavity-filling:", cavity_filling)
print("X-Ray:", x_ray)
print("Subtotal:", str(Bill))
print("Tax:", str(tax))
print(total)



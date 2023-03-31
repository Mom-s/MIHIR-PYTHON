#mihirs program
def calculate_bill(cleaning, cavity_filling, x_ray):
    subtotal = 0
    if cleaning == 'y':
        subtotal += 60
    if cavity_filling == 'y':
        subtotal += 200
    if x_ray == 'y':
        subtotal += 100
    tax = subtotal * 0.15
    total = subtotal + tax
    if total > 300:
        total *= 0.9
    elif total > 200:
        total *= 0.95
    return total

name = input("Enter patient's name: ")
cleaning = input("Was cleaning performed? (y/n): ")
cavity_filling = input("Was cavity-filling performed? (y/n): ")
x_ray = input("Was X-Ray performed? (y/n): ")

total = calculate_bill(cleaning, cavity_filling, x_ray)

print("Melanie Dental Clinic")
print("Patient name:", name)
print("Cleaning:", cleaning)
print("Cavity-filling:", cavity_filling)
print("X-Ray:", x_ray)
print("Subtotal:", '$' + str(subtotal))
print("Tax:", '$' + str(tax))
print("Total:", '$' + str(total))



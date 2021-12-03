import numpy as np

# Open data and put in list 
with open("data_day3.txt", "r") as file:
    data = [ [int(digit) for digit in line.split("\n")[0]] for line in file.readlines() ]
    
################################ First part #################################
digit_counter = np.sum(data, axis=0)

gamma = ""
epsilon = ""

for i in digit_counter:
    if i > len(data) // 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
        
print(f"gamma in binary = {int(gamma)} and in decimal = {int(gamma, 2)}")        
print(f"epsilon in binary = {int(epsilon)} and in decimal = {int(epsilon, 2)}") 

multiplier = int(gamma, 2) * int(epsilon, 2)
print(multiplier)

################################ Second part ################################

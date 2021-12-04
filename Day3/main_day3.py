import numpy as np

# Open data and put in list 
with open("data_day3.txt", "r") as file:
    data = [ [int(digit) for digit in line.split("\n")[0]] for line in file.readlines() ]
    
################################ First part #################################
# Sums all the columns
digit_counter = np.sum(data, axis=0)

# Define empty gamma and epsilon that will be filled later with binary digits
gamma = ""
epsilon = ""

# if the i-th sum of the digit is larger than the average of the data-set, than gamma=1 and epsilon=0
for i in digit_counter:
    if i > len(data) // 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

# Print gamma and epsilon in decimals and multiply them together        
print(f"gamma in binary = {gamma} and in decimal = {int(gamma, 2)}")        
print(f"epsilon in binary = {epsilon} and in decimal = {int(epsilon, 2)}") 

multiplier = int(gamma, 2) * int(epsilon, 2)
print(multiplier)


################################ Second part ################################
def molecule_binary_check(molecule, data):
    new_data = data.copy() 
    
    # Check input of molecule and changes state for later use
    if molecule == "O2":
        state = 0
    elif molecule == "CO2":
        state = 1
    else:
        return print("Invalid molecule")
    
    # Loop over the digit 
    for digit in range(len(new_data[0])):
        total = np.sum(new_data, axis=0)
        length_data = len(new_data)
        later_changed_data = new_data.copy()
        
        # Check if loop has to end
        if len(later_changed_data) == 1:
            break
        
        # If there are more 1's than 0's with 02, than it removes the lists that have a digit of 0.
        # And for CO2 it is vice versa.
        if total[digit] >= length_data / 2:
            for x in later_changed_data:
                if x[digit] == state:
                    new_data.remove(x) 
         
        # If there are more 0's than 1's with 02, than it removes the lists that have a digit of 1.
        # And for CO2 it is vice versa. 
        else:
            for y in later_changed_data:
                if y[digit] != state:
                    new_data.remove(y)
                    
    return new_data[0]

# Uses the function of above and transforms the list output of the function into a string
O2 = "".join([str(m) for m in molecule_binary_check("O2", data)])
CO2 = "".join([str(n) for n in molecule_binary_check("CO2", data)])

print(f"O2 in binary = {O2} and in decimal = {int(O2, 2)}")        
print(f"CO2 in binary = {CO2} and in decimal = {int(CO2, 2)}") 

# Multiplies the decimal numbers
multiplier_2 = int(O2, 2) * int(CO2, 2)
print(multiplier_2)
    

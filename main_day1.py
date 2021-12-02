# Open data and put in list 
with open("data_day1.txt", "r") as file:
    numbers = [int(num) for num in file.readlines()]


################################ First part #################################    
counter_1 = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        counter_1 += 1

print(counter_1)

################################ Second part #################################
counter_2 = 0

for i in range(1, len(numbers)):
    if sum( numbers[i:i+3] ) > sum( numbers[i-1:i+2] ):
        counter_2 += 1

print(counter_2)
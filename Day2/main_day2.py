# Open data and put in list 
with open("data_day2.txt", "r") as file:
    directions = [line.split(" ") for line in file.readlines()]

################################ First part #################################
horizontal_position = 0
depth = 0

for move in directions:
    if move[0] == "forward":
        horizontal_position += int(move[1])
    elif move[0] == "up":
        depth -= int(move[1])
    elif move[0] == "down":
        depth += int(move[1])

multiplication = horizontal_position * depth
print(multiplication)

################################ Second part #################################
horizontal_position_2 = 0
depth_2 = 0
aim = 0

for move in directions:
    if move[0] == "forward":
        horizontal_position_2 += int(move[1])
        depth_2 += int(move[1]) * aim
    elif move[0] == "up":
        aim -= int(move[1])
    elif move[0] == "down":
        aim += int(move[1])

multiplication_2 = horizontal_position_2 * depth_2
print(multiplication_2)

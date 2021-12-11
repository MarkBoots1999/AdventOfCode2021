with open("Day10/input10.txt", "r") as file:
    data = file.read().splitlines()

allowed_match = {"(": ")",
                 "[": "]",
                 "{": "}",
                 "<": ">"}

match_score = {")": 3,
               "]": 57,
               "}": 1197,
               ">": 25137}

closing_score = {")": 1,
                 "]": 2,
                 "}": 3,
                 ">": 4}

# Score part 1
score = 0
# For part 2
score_array = []

for line in data:
    # Ignore incomplete lines by resetting them every iteration
    stack = []
     
    for sign in line:
        if sign in "([{<":
            stack.append(sign)
        else:
            if sign == allowed_match[stack[-1]]:
                stack.pop()
            elif stack == [] or sign != allowed_match[stack[-1]]:
                score += match_score[sign]
                stack.clear()
                # Break after first encountered error in line
                break 
    
    # Part 2        
    score_2 = 0    
    
    if stack:
        for element in reversed(stack):
            score_2 = 5 * score_2 + closing_score[ allowed_match[element] ]
        
        score_array.append(score_2)
        
middle_value = sorted(score_array)[len(score_array)//2]
print(f"Score Part 1 {score}")
print(f"Score Part 2 {middle_value}")

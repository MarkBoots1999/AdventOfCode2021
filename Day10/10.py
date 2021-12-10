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


score = 0

for line in data:
    stack = [] # Ignore incomplete lines by resetting them every iteration
    for sign in line:
        #print(stack)
        if sign in "([{<":
            stack.append(sign)
        else:
            if sign == allowed_match[stack[-1]]: #stack == None or 
                #print(f"closed {allowed_match[stack[-1]]}")
                stack.pop()
            elif stack == None or sign != allowed_match[stack[-1]]:
                #print(f"{sign} error")    
                score += match_score[sign]
                break # Break after first error in line
print(score)

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

stack = []
score = 0

for line in data:
    for sign in line:
        if sign in "([{<":
            stack.append(sign)
        else:
            if stack == None or stack[-1] != allowed_match.get(sign):
                print(allowed_match.get_key(sign))
                score += match_score[sign] 
            else:
                stack.pop()
    break

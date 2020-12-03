from math import sqrt
action = input("what do you wanna do bro? ")

if action == "calculator":
    operation = input("operation? ")
    num1 = int(input("whats the first number dude? "))
    num2 = int(input("whats the second number bro? "))
    answer = 0
    if operation == "+":
        answer = num1 + num2
        print('Answer is: ' + str(answer))
    elif operation == "-":
        answer = num1 - num2
        print('Answer is: ' + str(answer))
    elif operation == "*":
        answer = num1 * num2
        print('Answer is: ' + str(answer))
    elif operation == "/":
        answer = num1 / num2
        print('Answer is: ' + str(answer))
    elif operation == "%":
        answer = num1 % num2
        print('Answer is: ' + str(answer))
    else:
        print("are you sure about that or are you just really dumb")
elif action == "perimeter":
    peri_answer = 0
    rec_or_squ = input("square or rectangle broooo? ")
    if rec_or_squ == "rectangle":
        rec_leng = int(input("whats is the length of the rectangle dudebro? "))
        rec_brea = int(input("whats the breadth of the rectangle dudebroboy? "))
        peri_answer = 2*(rec_leng+rec_brea)
    elif rec_or_squ == "square":
        squ_side = int(input("whats the side of the square huh? "))
        peri_answer = squ_side*4
        print("The Answer is: " + str(peri_answer)+(" units"))
elif action == "area":
    area_answer = 0
    area__rec_or_squ = input("square or rectangle dude? ")
    if area__rec_or_squ == "rectangle":
        area__rec_leng = int(input("what is the length of rectangle dude? "))
        area__rec_brea = int(input("what is the breadth of the rectangle dudebroguy? "))
        area_answer = area__rec_leng*area__rec_brea
        print("The answer is: " + str(area_answer) + (" units"))
    elif area__rec_or_squ == "square":
        area__squ_side = int(input("what is the side of the square broooooo? "))
        area_answer = area__squ_side*area__squ_side
        print("The Answer is: " + str(area_answer) + (" units"))
elif action == "square root":
    square_root = input("hey whats the square root? ")
    squ_root = sqrt(int(square_root))
    print((squ_root))
else:
    print("check your spelling cuz idk wtf that means")

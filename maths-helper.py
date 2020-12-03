from math import sqrt
action = input("What do you want me to do? ")

if action == "calculator":
    operation = input("operation? ")
    num1 = float(input("First Number? "))
    num2 = float(input("Second Number? "))
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
        print("Not sure what to do there. Check if you have any typos.")
elif action == "perimeter":
    peri_answer = 0
    rec_or_squ = input("Square or Rectangle? ")
    if rec_or_squ == "rectangle":
        rec_leng = float(input("What is the length of the rectangle? "))
        rec_brea = float(input("What is the breadth of the rectangle? "))
        peri_answer = 2*(rec_leng+rec_brea)
    elif rec_or_squ == "square":
        squ_side = float(input("What is the side of the square? "))
        peri_answer = squ_side*4
        print("The Answer is: " + str(peri_answer)+(" units"))
elif action == "area":
    area_answer = 0
    area__rec_or_squ = input("Square or Rectangle? ")
    if area__rec_or_squ == "rectangle":
        area__rec_leng = float(input("What is the length of the rectangle? "))
        area__rec_brea = float(input("What is the breadth of the rectangle? "))
        area_answer = area__rec_leng*area__rec_brea
        print("The answer is: " + str(area_answer) + (" units"))
    elif area__rec_or_squ == "square":
        area__squ_side = float(input("What is the side of the square? "))
        area_answer = area__squ_side*area__squ_side
        print("The Answer is: " + str(area_answer) + (" units"))
elif action == "square root":
    square_root = input("What is the number you want to find the square root of? ")
    squ_root = sqrt(float(square_root))
    print(squ_root)
else:
    print("Not sure what to do there. Check if you have any typos.")

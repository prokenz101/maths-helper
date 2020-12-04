from math import sqrt
action = input("What do you want me to do? ")

if action == "calculator":
    operation = input("Operation? ")
    if operation == "quit":
        exit()
    num1 = input("What is the first number? ")
    if num1 == "quit":
        exit()
    num2 = input("What is the second number? ")
    if num2 == "quit":
        exit()
    answer = 0
    if operation == "+":
        answer = float(num1) + float(num2)
        print('Answer is: ' + str(answer))
    elif operation == "-":
        answer = float(num1) - float(num2)
        print('Answer is: ' + str(answer))
    elif operation == "*":
        answer = float(num1) * float(num2)
        print('Answer is: ' + str(answer))
    elif operation == "/":
        answer = float(num1) / float(num2)
        print('Answer is: ' + str(answer))
    elif operation == "%":
        answer = float(num1) % float(num2)
        print('Answer is: ' + str(answer))
elif action == "perimeter":
    peri_answer = 0
    rec_or_squ = input("Square or Rectangle? ")
    if rec_or_squ == "quit":
        exit()
    if rec_or_squ == "rectangle":
        rec_leng = input("What is the length of the rectangle? ")
        if rec_leng == "quit":
            exit()
        rec_brea = input("What is the breadth of the rectangle? ")
        if rec_brea == "quit":
            exit()
        peri_answer = 2 * (float(rec_leng) + float(rec_brea))
        print(f'The Answer is: {peri_answer} units')
    elif rec_or_squ == "square":
        squ_side = input("What is the side of the square? ")
        if squ_side == "quit":
            exit()
        peri_answer = float(squ_side) * 4
        print("The Answer is: " + str(peri_answer)+(" units"))
elif action == "area":
    area_answer = 0
    area__rec_or_squ = input("Square or Rectangle? ")
    if area__rec_or_squ == "quit":
        exit()
    else:
        if area__rec_or_squ == "rectangle":
            if area__rec_or_squ == "quit":
                exit()
            area__rec_leng = input("What is the length of the rectangle? ")
            if area__rec_leng == "quit":
                exit()
            area__rec_brea = input("What is the breadth of the rectangle? ")
            if area__rec_brea == "quit":
                exit()
            area_answer = float(area__rec_leng) * float(area__rec_brea)
            print("The Answer is: " + str(area_answer) + (" square units"))
        elif area__rec_or_squ == "square":
            area__squ_side = input("What is the side of the square? ")
            if area__squ_side == "quit":
                exit()
            area_answer = float(area__squ_side) * float(area__squ_side)
            print("The Answer is: " + str(area_answer) + (" square units"))
elif action == "square root":
    square_root = input("What is the number you want to find the square root of? ")
    if square_root == "quit":
        exit()
    else:
        squ_root = sqrt(float(square_root))
        print(f'The Answer is: {squ_root}')
elif action == "pythagorean theorem":
    altitude__y_or_no = input("Do you have the altitude? ")
    base__y_or_no = input("Do you have the base? ")
    hypotenuse__y_or_no = input("Do you have the hypotenuse? ")
    answer = None
    altitude = None
    base = None
    hypotenuse = None
    if altitude__y_or_no == "yes":
        altitude = input("What is the altitude? ")
    if base__y_or_no == "yes":
        base = input("What is the base? ")
    if hypotenuse__y_or_no == "yes":
        hypotenuse = input("What is the hypotenuse? ")
    if altitude__y_or_no == "yes" and base__y_or_no == "yes" and hypotenuse__y_or_no == "no":
        answer = sqrt((float(altitude) * float(altitude)) + (float(base) * float(base)))
    elif hypotenuse__y_or_no == "yes" and base__y_or_no == "yes" and altitude__y_or_no == "no": 
        answer = sqrt((float(hypotenuse) * float(hypotenuse)) - (float(base) * float(base)))
    elif hypotenuse__y_or_no == "yes" and altitude__y_or_no == "yes" and base__y_or_no == "no":
        answer = sqrt((float(hypotenuse) * float(hypotenuse)) - (float(altitude) * float(altitude)))
    print(f'The Answer Is: {answer}')
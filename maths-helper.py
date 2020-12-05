from math import pi, sqrt
number_pi = pi
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
    rec_or_squ_or_cir = input("Square or Rectangle or Circle? ")
    if rec_or_squ_or_cir == "quit":
        exit()
    if rec_or_squ_or_cir == "rectangle":
        rec_leng = input("What is the length of the rectangle? ")
        if rec_leng == "quit":
            exit()
        rec_brea = input("What is the breadth of the rectangle? ")
        if rec_brea == "quit":
            exit()
        peri_answer = 2 * (float(rec_leng) + float(rec_brea))
        print(f'The Answer is: {peri_answer} units')
    elif rec_or_squ_or_cir == "square":
        squ_side = input("What is the side of the square? ")
        if squ_side == "quit":
            exit()
        peri_answer = float(squ_side) * 4
        print("The Answer is: " + str(peri_answer)+(" units"))
    elif rec_or_squ_or_cir == "circle":
        cir_radi = input("What is the radius of the circle? ")
        if cir_radi == "quit":
            exit()
        peri_answer = number_pi * float(cir_radi) * float(cir_radi)
        print(f'The Answer Is: {peri_answer}')
elif action == "area":
    area_answer = 0
    area__rec_or_squ_or_cir = input("Square or Rectangle or Circle? ")
    if area__rec_or_squ_or_cir == "quit":
        exit()
    else:
        if area__rec_or_squ_or_cir == "rectangle":
            if area__rec_or_squ_or_cir == "quit":
                exit()
            area__rec_leng = input("What is the length of the rectangle? ")
            if area__rec_leng == "quit":
                exit()
            area__rec_brea = input("What is the breadth of the rectangle? ")
            if area__rec_brea == "quit":
                exit()
            area_answer = float(area__rec_leng) * float(area__rec_brea)
            print("The Answer is: " + str(area_answer) + (" square units"))
        elif area__rec_or_squ_or_cir == "square":
            area__squ_side = input("What is the side of the square? ")
            if area__squ_side == "quit":
                exit()
            area_answer = float(area__squ_side) * float(area__squ_side)
            print("The Answer is: " + str(area_answer) + (" square units"))
        elif area__rec_or_squ_or_cir == "circle":
            area_diam = input("What is the diameter of the circle? ")
            if area_diam == "quit":
                exit()
            area_answer = (pi/4) * float(area_diam) * float(area_diam)
            print(f'The Answer Is: {area_answer} square units')
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
        print(f'The Answer Is: {answer}')
    elif hypotenuse__y_or_no == "yes" and base__y_or_no == "yes" and altitude__y_or_no == "no": 
        answer = sqrt((float(hypotenuse) * float(hypotenuse)) - (float(base) * float(base)))
        print(f'The Answer Is: {answer}')
    elif hypotenuse__y_or_no == "yes" and altitude__y_or_no == "yes" and base__y_or_no == "no":
        answer = sqrt((float(hypotenuse) * float(hypotenuse)) - (float(altitude) * float(altitude)))
        print(f'The Answer Is: {answer}')
    elif hypotenuse__y_or_no == "yes" and altitude__y_or_no == "yes" and base__y_or_no == "yes":
        print("Why are you asking me if you already have all 3 sides?")
    
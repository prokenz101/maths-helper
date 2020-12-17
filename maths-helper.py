from math import pi, sqrt, gcd
app_state = "active"
while app_state == "active":
    action = input("What do you want me to do? ")
    useable_commands = ['The Useable Commands are:', 'calculator',
                        'perimeter / p', 'area / a', 'square root / s', 'cube root / cr', 'pythagorean theorem / pt']

    if action == "help":
        print("Need Help? Try 'commands' for a list of commands.")
        print("If you still need help, then go to github.com/prokenz101/maths-helper and read the README.md.")
    if action == "q" or action == "quit":
        exit()
    if action == "commands":
        for displayed_commands in useable_commands:
            print(displayed_commands)
    while action == "calculator" or action == "c":
        operation = input("Operation? Press Q to quit. ")
        if operation == "quit" or operation == "q":
            exit()
        if operation == "..":
            break
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
    while action == "perimeter" or action == "p":
        peri_answer = 0
        rec_or_squ_or_cir_or_tria_or_paral = input(
            "Square or Rectangle or Circle or Triangle or Parallelogram? Press Q to quit. ")
        if rec_or_squ_or_cir_or_tria_or_paral == "quit" or rec_or_squ_or_cir_or_tria_or_paral == "q":
            exit()
        elif rec_or_squ_or_cir_or_tria_or_paral == "..":
            break
        while rec_or_squ_or_cir_or_tria_or_paral == "rectangle":
            rec_leng = input("What is the length of the rectangle? ")
            if rec_leng == "quit" or rec_leng == "q":
                exit()
            elif rec_leng == "..":
                break
            rec_brea = input("What is the breadth of the rectangle? ")
            if rec_brea == "quit" or rec_brea == "q":
                exit()
            elif rec_brea == "..":
                break
            peri_answer = 2 * (float(rec_leng) + float(rec_brea))
            print(f'The Answer is: {peri_answer} units')
        while rec_or_squ_or_cir_or_tria_or_paral == "square":
            squ_side = input("What is the side of the square? ")
            if squ_side == "quit" or squ_side == "q":
                exit()
            elif squ_side == "..":
                break
            peri_answer = float(squ_side) * 4
            print("The Answer is: " + str(peri_answer)+(" units"))
        while rec_or_squ_or_cir_or_tria_or_paral == "circle":
            cir_radi = input("What is the radius of the circle? ")
            if cir_radi == "quit" or cir_radi == "q":
                exit()
            elif cir_radi == "..":
                break
            peri_answer = pi * float(cir_radi) * float(cir_radi)
            print(f'The Answer Is: {peri_answer}')
        while rec_or_squ_or_cir_or_tria_or_paral == "triangle":
            tria_base_peri = input("What is the base of the triangle? ")
            tria_side_peri = input("What is the side of the triangle? ")
            tria_peri = float(tria_base_peri) + \
                float(tria_side_peri) + float(tria_side_peri)
            print(f'The Answer Is: {tria_peri}')
        while rec_or_squ_or_cir_or_tria_or_paral == "parallelogram":
            paral_base_peri = input("What is the base of the parallelogram? ")
            paral_side_peri = input("What is the side of the parallelogram? ")
            paral_peri = 2*(float(paral_base_peri) + float(paral_side_peri))
            print(f'The Answer Is: {paral_peri}')
    while action == "area" or action == "a":
        area_answer = 0
        area__rec_or_squ_or_cir_or_tria_or_paral = input(
            "Square or Rectangle or Circle or Triangle or Parallelogram? Press Q to quit. ")
        if area__rec_or_squ_or_cir_or_tria_or_paral == "quit" or area__rec_or_squ_or_cir_or_tria_or_paral == "q":
            exit()
        elif area__rec_or_squ_or_cir_or_tria_or_paral == "..":
            break
        else:
            if area__rec_or_squ_or_cir_or_tria_or_paral == "rectangle":
                if area__rec_or_squ_or_cir_or_tria_or_paral == "quit" or area__rec_or_squ_or_cir_or_tria_or_paral == "q":
                    exit()
                elif area__rec_or_squ_or_cir_or_tria_or_paral == "..":
                    break
                area__rec_leng = input("What is the length of the rectangle? ")
                if area__rec_leng == "quit" or area__rec_leng == "q":
                    exit()
                elif area__rec_or_squ_or_cir_or_tria_or_paral == "..":
                    break
                area__rec_brea = input("What is the breadth of the rectangle? ")
                if area__rec_brea == "quit" or area__rec_brea == "q":
                    exit()
                elif area__rec_brea == "..":
                    break
                area_answer = float(area__rec_leng) * float(area__rec_brea)
                print("The Answer is: " + str(area_answer) + (" square unit(s)"))
            elif area__rec_or_squ_or_cir_or_tria_or_paral == "square":
                area__squ_side = input("What is the side of the square? ")
                if area__squ_side == "quit" or area__squ_side == "q":
                    exit()
                elif area__squ_side == "..":
                    break
                area_answer = float(area__squ_side) * float(area__squ_side)
                print("The Answer is: " + str(area_answer) + (" square unit(s)"))
            elif area__rec_or_squ_or_cir_or_tria_or_paral == "circle":
                area_diam = input("What is the diameter of the circle? ")
                if area_diam == "quit" or area_diam == "q":
                    exit()
                elif area_diam == "..":
                    break
                area_answer = (pi/4) * float(area_diam) * float(area_diam)
                print(f'The Answer Is: {area_answer} square unit(s)')
            elif area__rec_or_squ_or_cir_or_tria_or_paral == "triangle":
                tria_height = input("What is the height of the triangle? ")
                tria_base = input("What is the base of the triangle? ")
                tria_area = (float(tria_height)*float(tria_base))/2
                print(f'The Answer Is: {tria_area} sq unit(s)')
            elif area__rec_or_squ_or_cir_or_tria_or_paral == "parallelogram":
                paral_height = input("What is the height of the parallelogram? ")
                paral_base = input("What is the base of the parallelogram? ")
                paral_area = float(paral_height)*float(paral_base)
                print(f'The Answer Is: {paral_area} sq unit(s)')
    while action == "square root" or action == "s":
        square_root = input(
            "What is the number you want to find the square root of? Press Q to quit. ")
        if square_root == "quit" or square_root == "q":
            exit()
        elif square_root == "..":
            break
        else:
            squ_root = sqrt(float(square_root))
            print(f'The Answer is: {squ_root}')
    while action == "cube root" or action == "cr":
        cube_root = input(
            "What is the number that you want me to find the cube root of? ")
        cube_root_answer = float(cube_root) ** (1/3)
        print(f'The Answer Is: {cube_root_answer}')
        if cube_root == "quit" or cube_root == "q":
            exit()
        elif cube_root == "..":
            break
    while action == "pythagorean theorem" or action == "pt":
        altitude__y_or_no = input("Do you have the altitude? ")
        if altitude__y_or_no == "quit" or altitude__y_or_no == "q":
            exit()
        base__y_or_no = input("Do you have the base? ")
        if base__y_or_no == "quit" or base__y_or_no == "q":
            exit()
        hypotenuse__y_or_no = input("Do you have the hypotenuse? ")
        if hypotenuse__y_or_no == "quit" or hypotenuse__y_or_no == "q":
            exit()
        answer = None
        altitude = None
        base = None
        hypotenuse = None
        if altitude__y_or_no == "yes":
            altitude = input("What is the altitude? ")
        elif altitude == "..":
            break
        if base__y_or_no == "yes":
            base = input("What is the base? ")
        elif base == "..":
            break
        if hypotenuse__y_or_no == "yes":
            hypotenuse = input("What is the hypotenuse? ")
        elif hypotenuse == "..":
            break
        if altitude__y_or_no == "yes" and base__y_or_no == "yes" and hypotenuse__y_or_no == "no":
            answer = sqrt((float(altitude) * float(altitude)) +
                        (float(base) * float(base)))
            print(f'The Answer Is: {answer}')
        elif hypotenuse__y_or_no == "yes" and base__y_or_no == "yes" and altitude__y_or_no == "no":
            answer = sqrt((float(hypotenuse) * float(hypotenuse)) -
                        (float(base) * float(base)))
            print(f'The Answer Is: {answer}')
        elif hypotenuse__y_or_no == "yes" and altitude__y_or_no == "yes" and base__y_or_no == "no":
            answer = sqrt((float(hypotenuse) * float(hypotenuse)) -
                        (float(altitude) * float(altitude)))
            print(f'The Answer Is: {answer}')
        elif hypotenuse__y_or_no == "yes" and altitude__y_or_no == "yes" and base__y_or_no == "yes":
            print("Why are you asking me if you already have all 3 sides?")
    while action == "HCF" or action == "hcf":
        hcf__fir_num = input("What is the first number? Press Q to quit. ")
        if hcf__fir_num == "quit" or hcf__fir_num == "q":
            exit()
        elif hcf__fir_num == "..":
            break
        else:
            hcf__sec_num = input("What is the second number? ")
        if hcf__sec_num == "quit" or hcf__sec_num == "q":
            exit()
        elif hcf__sec_num == "..":
            break
        else:
            hcf_answer = gcd(int(hcf__fir_num), int(hcf__sec_num))
        print(f'The Answer Is {hcf_answer}')

from math import pi, sqrt, gcd
quit_list = [
    "quit",
    "q",
    "exit"
]

def get_float(message):
    while True:
        x = input(message)
        if x.lower() in quit_list:
            exit()
        try:
            converted = float(x)
            return converted
        except ValueError:
            print("Please enter a number, and not anything else. Press Q to quit.")


def addition(first, second):
    first = get_float("What is the first number? ")
    second = get_float("What is the second number? ")
    answer = first + second
    print(f'The Answer Is: {answer}')


def subtraction(first, second):
    first = get_float("What is the first number? ")
    num_2 = get_float("What is the second number? ")
    answer = first - second
    print(f'The Answer Is: {answer}')


def multiplication(first, second):
    first = get_float("What is the first number? ")
    second = get_float("What is the second number? ")
    answer = first * second
    print(f'The Answer Is: {answer}')


def division(first, second):
    first = get_float("What is the first number? ")
    second = get_float("What is the second number? ")
    answer = first / second
    print(f'The Answer Is: {answer}')


def remainder(first, second):
    first = get_float("What is the first number? ")
    second = get_float("What is the second number? ")
    answer = first % second
    print(f'The Answer Is: {answer}')


def perimeter_rectangle(first, second):
    first = get_float("What is the length of the rectangle? ")
    second = get_float("What is the breadth of the rectangle? ")
    if second == "quit" or second == "q":
        exit()
    peri_answer = (first) + (second)*2
    print(f'The Answer Is: {peri_answer} unit(s)')


def perimeter_square(first):
    first = get_float("What is the side of the square? ")
    peri_answer = first*4
    print(f'The Answer Is: {peri_answer} unit(s)')


def perimeter_circle(first):
    first = get_float("What is the radius of the circle? ")
    peri_answer = (pi * 2) * first
    print(f'The Answer Is: {peri_answer} unit(s)')


def perimeter_triangle(first, second, third):
    first = get_float("What is the side of the triangle? ")
    second = get_float("What is the base of the triangle? ")
    third = get_float("What is the side of the triangle(2)? ")
    peri_answer = (float(second) + float(third)) + float(first)
    print(f'The Answer Is: {peri_answer} unit(s)')


def perimeter_parallelogram(first, second):
    first = get_float("What is the base of the parallelogram? ")
    second = get_float("What is the side of the parallelogram? ")
    peri_answer = 2 * (first + second)
    print(f'The Answer Is: {peri_answer} unit(s)')


def area_rectangle(first, second):
    first = get_float("What is the length of the rectangle? ")
    second = get_float("What is the breadth of the rectangle? ")
    area_answer = 2*(first + second)
    print(f'The Answer Is: {area_answer} square unit(s)')


def area_square(first):
    first = get_float("What is the side of the square? ")
    area_answer = first * first
    print(f'The Answer Is: {area_answer} square unit(s)')


def area_circle(first):
    first = get_float("What is the diameter of the circle? ")
    area_answer = (pi/4) * first * first


def area_triangle(first, second):
    first = get_float("What is the base of the triangle? ")
    second = get_float("What is the height of the triangle? ")
    area_answer = (first*second)/2
    print(f'The Answer Is: {area_answer} square unit(s)')


def area_parallelogram(first, second):
    first = get_float("What is the base of the parallelogram? ")
    second = get_float("What is the height of the parallelogram? ")
    area_answer = first * second
    print(f'The Answer Is: {area_answer} square unit(s)')


def square_root(first):
    first = get_float("What is the number that you want me to find the square root of? ")
    square_root_answer = sqrt(first)
    print(f'The Answer Is: {square_root_answer}')


def cube_root(first):
    first = get_float("What is the number that you want me to find the cube root of? ")
    cube_root_answer = first ** (1/3)
    print(f'The Answer Is: {cube_root_answer}')


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

   # Calculator

    while action.lower() in ["calculator", "c", "69"]:
        operation = input("Operation? Press Q to quit. ")
        if operation.lower() in quit_list:
            exit()
        if operation == "..":
            break
        answer = None
        num_1 = None
        num_2 = None
        if operation == "+":
            try:
                addition(num_1, num_2)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        elif operation == "-":
            try:
                subtraction(num_1, num_2)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        elif operation == "*":
            try:
                multiplication(num_1, num_2)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        elif operation == "/":
            try:
                division(num_1, num_2)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        elif operation == "%":
            try:
                remainder(num_1, num_2)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")

    # Perimeter

    while action == "perimeter" or action == "p":
        peri_answer = None
        rec_or_squ_or_cir_or_tria_or_paral = input(
            "Square or Rectangle or Circle or Triangle or Parallelogram? Press Q to quit. ")
        if rec_or_squ_or_cir_or_tria_or_paral == "quit" or rec_or_squ_or_cir_or_tria_or_paral == "q":
            exit()
        elif rec_or_squ_or_cir_or_tria_or_paral == "..":
            break
        while rec_or_squ_or_cir_or_tria_or_paral == "rectangle":
            rec_leng = None
            rec_brea = None
            try:
                perimeter_rectangle(rec_leng, rec_brea)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        while rec_or_squ_or_cir_or_tria_or_paral == "square":
            peri_squ_side = None
            try:
                perimeter_square(peri_squ_side)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        while rec_or_squ_or_cir_or_tria_or_paral == "circle":
            cir_radi = None
            try:
                perimeter_circle(cir_radi)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        while rec_or_squ_or_cir_or_tria_or_paral == "triangle":
            tria_peri_side_1 = None
            tria_base_peri = None
            tria_peri_side_2 = None
            try:
                perimeter_triangle(
                    tria_base_peri, tria_peri_side_1, tria_peri_side_2)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        while rec_or_squ_or_cir_or_tria_or_paral == "parallelogram":
            paral_side_peri = None
            paral_base_peri = None
            try:
                perimeter_parallelogram(paral_base_peri, paral_side_peri)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")

    # Area

    while action == "area" or action == "a":
        area_answer = None
        area__rec_or_squ_or_cir_or_tria_or_paral = input(
            "Square or Rectangle or Circle or Triangle or Parallelogram? Press Q to quit. ")
        if area__rec_or_squ_or_cir_or_tria_or_paral == "quit" or area__rec_or_squ_or_cir_or_tria_or_paral == "q":
            exit()
        elif area__rec_or_squ_or_cir_or_tria_or_paral == "..":
            break
        while area__rec_or_squ_or_cir_or_tria_or_paral == "rectangle":
            area_rec_leng = None
            area_rec_brea = None
            try:
                area_rectangle(area_rec_leng, area_rec_brea)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        while area__rec_or_squ_or_cir_or_tria_or_paral == "square":
            area_squ_side = None
            try:
                area_square(area_squ_side)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        while area__rec_or_squ_or_cir_or_tria_or_paral == "circle":
            area_cir_diam = None
            try:
                area_circle(area_cir_diam)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        while area__rec_or_squ_or_cir_or_tria_or_paral == "triangle":
            area_tria_base = None
            area_tria_height = None
            try:
                area_triangle(area_tria_base, area_tria_height)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")
        while area__rec_or_squ_or_cir_or_tria_or_paral == "parallelogram":
            area_paral_base = None
            area_paral_height = None
            try:
                area_parallelogram(area_paral_base, area_paral_height)
            except ValueError:
                print("Please enter a number, and not anything else. Press Q to quit.")

    # Square Root

    while action == "square root" or action == "s":
        square_root_num = None
        square_root(square_root_num)

    # Cube Root

    while action == "cube root" or action == "cr":
        cube_root_num = None
        cube_root(cube_root_num)

    # Pythagorean Theorem

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

    # HCF

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

    # LCM

    while action == "LCM" or action == "lcm":
        lcm_num_1 = input("What is the first number? ")
        if lcm_num_1 == "quit" or lcm_num_1 == "q":
            exit()
        elif lcm_num_1 == "..":
            break
        lcm_num_2 = input("What is the second number? ")
        if lcm_num_2 == "quit" or lcm_num_2 == "q":
            exit()
        elif lcm_num_2 == "..":
            break
        lcm_hcf = gcd(int(lcm_num_1), int(lcm_num_2))
        lcm = int(lcm_num_1) * int(lcm_num_2)/int(lcm_hcf)
        print(f'The Answer Is: {lcm}')
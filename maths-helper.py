from math import pi, sqrt, gcd
import re
quit_list = [
    "quit",
    "q",
    "exit"
    "back"
    "leave"
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
    second = get_float("What is the second number? ")
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


def vol_cuboid(first, second, third):
    first = get_float("What is the length of the rectangle? ")
    second = get_float("What is the breadth of the rectangle? ")
    third = get_float("What is the height of the rectangle? ")
    vol_answer = first * second * third
    print(f'The Answer Is: {vol_answer} cubic unit(s)')


def vol_cube(first):
    first = get_float("What is the side of the square? ")
    vol_answer = first * first * first
    print(f'The Answer Is: {vol_answer} cubic unit(s)')


def vol_sphere(first):
    first = get_float("What is the radius of the circle? ")
    vol_answer = (4/3)*pi*(first * first * first)
    print(f'The Answer Is: {vol_answer} cubic unit(s)')


def vol_triaprism(first, second, third, fourth):
    first = get_float("What is the base side 1 of the triaprism? ")
    second = get_float("What is the base side 2 of the triaprism? ")
    third = get_float("What is the base side 3 of the triaprism? ")
    fourth = get_float("What is the height of the triaprism? ")
    vol_answer = ((1/4)*fourth) * sqrt((first + second + third) * (second +
                                                                   third - first) * (third + first - second) * (first + second - third))
    print(f'The Answer Is: {vol_answer} cubic unit(s)')


def square_root(first):
    first = get_float(
        "What is the number that you want me to find the square root of? ")
    square_root_answer = sqrt(first)
    print(f'The Answer Is: {square_root_answer}')


def cube_root(first):
    first = get_float(
        "What is the number that you want me to find the cube root of? ")
    cube_root_answer = first ** (1/3)
    print(f'The Answer Is: {cube_root_answer}')


def hyp(first, second):
    first = get_float("What is the altitude? ")
    second = get_float("What is the base? ")
    hyp_answer = sqrt((float(first) * float(first)) +
                      (float(second) * float(second)))
    print(f'The Answer Is: {hyp_answer}')


def alt(first, second):
    first = get_float("What is the hypotenuse? ")
    second = get_float("What is the base? ")
    alt_answer = sqrt((float(first) * float(first)) -
                      (float(second) * float(second)))
    print(f'The Answer Is: {alt_answer}')


def base(first, second):
    first = get_float("What is the hypotenuse? ")
    second = get_float("What is the altitude? ")
    base_answer = sqrt((float(first) * float(first)) -
                       (float(second) * float(second)))
    print(f'The Answer Is: {base_answer}')


def hcf(first, second):
    first = get_float("What is the first number? ")
    second = get_float("What is the second number? ")
    hcf_answer = gcd(int(first), int(second))
    print(f'The Answer Is: {hcf_answer}')


def lcm(first, second):
    first = get_float("What is the first number? ")
    second = get_float("What is the second number? ")
    third = gcd(int(first), int(second))
    lcm = int(first) * int(second) / int(third)
    print(f'The Answer Is: {lcm}')


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

   # Fraction Calcultor

    while action.lower() in ["fraction calculator", "fc"]:
        f_operation = input("What is the operation? ")
        if f_operation.lower() in quit_list:
            exit()
        elif f_operation == "..":
            break

   # Calculator

    while action.lower() in ["calculator", "c"]:
        operation = input("Operation? Press Q to quit. ")
        if operation.lower() in quit_list:
            exit()
        elif operation == "..":
            break
        elif operation == "commands":
            useable_commands = [
                'The Useable Commands are:', '+', '-', '*', '/', '%']
            for displayed_commands in useable_commands:
                print(displayed_commands)
        answer = None
        num_1 = None
        num_2 = None
        while operation == "+":
            addition(num_1, num_2)
        while operation == "-":
            subtraction(num_1, num_2)
        while operation == "*":
            multiplication(num_1, num_2)
        while operation == "/":
            division(num_1, num_2)
        while operation == "%":
            remainder(num_1, num_2)
    # Perimeter

    while action.lower() in ['perimeter', 'p']:
        peri_answer = None
        peri__rec_squ_cir_tria_paral = input(
            "Square or Rectangle or Circle or Triangle or Parallelogram? Press Q to quit. ")
        if peri__rec_squ_cir_tria_paral == "quit" or peri__rec_squ_cir_tria_paral == "q":
            exit()
        elif peri__rec_squ_cir_tria_paral == "..":
            break
        while peri__rec_squ_cir_tria_paral == "rectangle":
            rec_leng = None
            rec_brea = None
            perimeter_rectangle(rec_leng, rec_brea)
        while peri__rec_squ_cir_tria_paral == "square":
            peri_squ_side = None
            perimeter_square(peri_squ_side)
        while peri__rec_squ_cir_tria_paral == "circle":
            cir_radi = None
            perimeter_circle(cir_radi)
        while peri__rec_squ_cir_tria_paral == "triangle":
            tria_peri_side_1 = None
            tria_base_peri = None
            tria_peri_side_2 = None
            perimeter_triangle(
                tria_base_peri, tria_peri_side_1, tria_peri_side_2)
        while peri__rec_squ_cir_tria_paral == "parallelogram":
            paral_side_peri = None
            paral_base_peri = None
            perimeter_parallelogram(paral_base_peri, paral_side_peri)

    # Area

    while action.lower() in ['area', 'a']:
        area_answer = None
        area__rec_squ_cir_tria_paral = input(
            "Square or Rectangle or Circle or Triangle or Parallelogram? Press Q to quit. ")
        if area__rec_squ_cir_tria_paral == "quit" or area__rec_squ_cir_tria_paral == "q":
            exit()
        elif area__rec_squ_cir_tria_paral == "..":
            break
        while area__rec_squ_cir_tria_paral == "rectangle":
            area_rec_leng = None
            area_rec_brea = None
            area_rectangle(area_rec_leng, area_rec_brea)
        while area__rec_squ_cir_tria_paral == "square":
            area_squ_side = None
            area_square(area_squ_side)
        while area__rec_squ_cir_tria_paral == "circle":
            area_cir_diam = None
            area_circle(area_cir_diam)
        while area__rec_squ_cir_tria_paral == "triangle":
            area_tria_base = None
            area_tria_height = None
            area_triangle(area_tria_base, area_tria_height)
        while area__rec_squ_cir_tria_paral == "parallelogram":
            area_paral_base = None
            area_paral_height = None
            area_parallelogram(area_paral_base, area_paral_height)

    # Volume

    while action.lower() in ['volume', 'v']:
        vol_answer = None
        vol__rec_squ_cir_tria_paral = input(
            "Cube or Cuboid or Sphere or Triangular Prism? Press Q to quit. ")
        if vol__rec_squ_cir_tria_paral.lower in quit_list:
            exit()
        elif vol__rec_squ_cir_tria_paral == "..":
            break
        while vol__rec_squ_cir_tria_paral == "cuboid":
            vol_cuboid_length = None
            vol_cuboid_breadth = None
            vol_cuboid_height = None
            vol_cuboid(vol_cuboid_length,
                       vol_cuboid_breadth, vol_cuboid_height)
        while vol__rec_squ_cir_tria_paral == "cube":
            vol_cube_side = None
            vol_cube(vol_cube_side)
        while vol__rec_squ_cir_tria_paral == "sphere":
            vol_sphere_radius = None
            vol_sphere(vol_sphere_radius)
        while vol__rec_squ_cir_tria_paral.lower() in ['triangular prism', 'tp']:
            vol_triaprism_base1 = None
            vol_triaprism_base2 = None
            vol_triaprism_base3 = None
            vol_triaprism_height = None
            vol_triaprism(vol_triaprism_base1, vol_triaprism_base2,
                          vol_triaprism_base3, vol_triaprism_height)

    # Square Root

    while action == "square root" or action == "s":
        square_root_num = None
        square_root(square_root_num)

    # Cube Root

    while action == "cube root" or action == "cr":
        cube_root_num = None
        cube_root(cube_root_num)

    # Hypotenuse

    while action == "hypotenuse" or action == "hyp":
        hyp_num_1 = None
        hyp_num_2 = None
        hyp(hyp_num_1, hyp_num_2)

    # Altitude

    while action == "altitude" or action == "alt":
        alt_num_1 = None
        alt_num_2 = None
        alt(alt_num_1, alt_num_2)

    # Base

    while action == "base":
        base_num_1 = None
        base_num_2 = None
        base(base_num_1, base_num_2)

    # HCF

    while action == "HCF" or action == "hcf":
        hcf_num_1 = None
        hcf_num_2 = None
        hcf(hcf_num_1, hcf_num_2)

    # LCM

    while action == "LCM" or action == "lcm":
        lcm_num_1 = None
        lcm_num_2 = None
        lcm(lcm_num_1, lcm_num_2)

    # Quick Commands
    
    while action.startswith("qc calculator") or action.startswith("qc c"):
        qc_question = action.split()
        if qc_question[1] == qc_question[3] == "+":
            qc_add_ans = float(qc_question[2]) + float(qc_question[4])
            print(f'The Answer Is: {qc_add_ans}')
            break
        elif qc_question[1] == qc_question[3] == "-":
            qc_subtract_ans = float(qc_question[2]) - float(qc_question[4])
            print(f'The Answer Is: {qc_subtract_ans}')
            break
        elif qc_question[1] == qc_question[3] == "*":
            qc_multiplicate_ans = float(qc_question[2]) * float(qc_question[4])
            print(f'The Answer Is: {qc_multiplicate_ans}')
            break
        elif qc_question[1] == qc_question[3] == "/":
            qc_divide_ans = float(qc_question[2]) / float(qc_question[4])
            print(f'The Answer Is: {qc_divide_ans}')
            break
        elif qc_question[1] == qc_question[3] == "%":
            qc_remainder_ans = float(qc_question[2]) % float(qc_question[4])
            print(f'The Answer Is: {qc_remainder_ans}')
            break
            
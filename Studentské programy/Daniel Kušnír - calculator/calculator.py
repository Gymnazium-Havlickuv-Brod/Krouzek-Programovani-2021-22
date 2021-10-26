import re

#num = "(9*5)-7**2+(4**3-16)" #((-3**9+65*(35*(-2)+3)/((-6*9)*(-3*7))+652)/2034//2)**2/35
num = input("Dej mi nějaký příklad :3  -->    ")
print("\n")
num_list = []
bracket_list = []
num_of_brackets = 0
used_symbol = -1


def multiply(st_number, nd_number):
    global result
    result = st_number * nd_number

def devide(st_number, nd_number):
    global result
    result = st_number / nd_number

def plus(st_number, nd_number):
    global result
    result = st_number + nd_number

def minus(st_number, nd_number):
    global result
    result = st_number - nd_number

def cube(st_number, nd_number):
    global result
    result = st_number ** nd_number

def cuberoot(st_number, nd_number):
    global result
    if st_number < 0: 
        st_number *= -1
    #result = round(st_number**(1/nd_number))
    result = st_number**(1/nd_number)

def math_problem_check():
    global string_detekt

    numbers_in_row = 0
    negative_number = 0
    same_operators = 0
    string_detekt = re.search("[a-žA-Ž]", num)
    if string_detekt != None:
        print("Příklad: " + num)
        print("\n")
        print("-----------------------------------------------------------------------------------------------")
        print("Nalezeno písmeno! S tím počítat neumím...")
        print("-----------------------------------------------------------------------------------------------")
    else:
        for i in range(len(num)):
            if num[i] != ' ':
                num_detekt = re.search("\d*\.*\d+", num[i])
                if num_detekt != None:
                    numbers_in_row += 1
                    if numbers_in_row == 1 and negative_number != 2: #and num_list[len(num_list) - 1] != "-":
                        num_list.append(num[i])
                        negative_number = 0
                    else:
                        num_list[len(num_list)-1] += num[i]
                        negative_number = 0
                    if negative_number >= 2:
                        num_list[len(num_list)-1] += num[i]
                elif num_detekt == None and num[i] != '*' and num[i] != '/':
                #print(num_detekt)
                    numbers_in_row = 0
                    num_list.append(num[i])

                    if num_list[0] == "-" and len(num_list) == 1:
                        negative_number = 2 
                    if num[i] == "(":
                        negative_number = 1
                    elif num[i] != "-":
                         negative_number = 0
                    if num_list[len(num_list) - 2] == "(" and num[i] == "-":
                        negative_number = 2 
                    elif num_list[len(num_list) - 2] == "(" and num[i] == "(":
                        negative_number = 1
                    elif num[i] != "-":
                        negative_number = 0
                elif num_list[len(num_list)-1] == num[i] and same_operators == 1 and num_detekt == None:
                    num_list[len(num_list)-1] += num[i]
                    same_operators = 0
                    numbers_in_row = 0
                else:
                    num_list.append(num[i])
                    same_operators = 1
                    numbers_in_row = 0


def bracket_identifier():
    global num_of_open_brackets
    global num_of_close_brackets 
    num_of_open_brackets = 0
    num_of_close_brackets = 0

    for i in num_list:
        if i == "(":
            num_of_open_brackets += 1
    for i in num_list:
        if i == ")":
            num_of_close_brackets += 1


def bracket_check():
    global st_post
    global nd_post
    global bracket_list

    bracket_list = []
    position = 0
    st_post = -1
    nd_post = -1
    for i in num_list:
        if i == "(":
            st_post = position
        if i == ")":
            nd_post = position
            break
        position += 1


def math_problem_printer():
    if len(num_list) == 1:
        math_problem = ''.join(num_list)
        print("-----------------------------------------------------------------------------------------------")
        print("Výsledek: " + math_problem)
        print("-----------------------------------------------------------------------------------------------")
    elif string_detekt == None and num_of_open_brackets == num_of_close_brackets and num_of_open_brackets >= 1 or num_of_open_brackets == 0:
        math_problem = ''.join(num_list)
        print("Příklad: " + math_problem)
        print(num_list)
        print("\n")

    if num_of_open_brackets != num_of_close_brackets:
        math_problem = ''.join(num_list)
        print("Příklad: " + math_problem)
        print("\n")
        print("-----------------------------------------------------------------------------------------------")
        print("Máš chybu v závorkách!")
        print("-----------------------------------------------------------------------------------------------")


def adding_to_bracket_list():
    global bracket

    for i in range(st_post + 1, nd_post):
        bracket_list.append(num_list[i])

    for i in range(st_post, nd_post + 1):
        num_list.pop(st_post)

    print("Závorky: " + str(st_post) + " - " + str(nd_post))
    bracket = ''.join(bracket_list)


def looking_for_cube_or_cuberoot(list):
    global used_symbol
    global symbol

    position = 0
    used_symbol = -1
    symbol = "nothing"
    for i in list:
        if i == '**' or i == '//':
            used_symbol = position
            symbol = i
            break
        else:
            symbol = "nothing"
        position += 1
    if symbol == '**':
        cube(float(list[used_symbol - 1]), float(list[used_symbol + 1]))
        for i in range(used_symbol - 1, used_symbol + 2):
            list.pop(used_symbol - 1)
        list.insert(used_symbol - 1, str(result))
    if symbol == '//':
        cuberoot(float(list[used_symbol - 1]), float(list[used_symbol + 1]))
        for i in range(used_symbol - 1, used_symbol + 2):
            list.pop(used_symbol - 1)
        list.insert(used_symbol - 1, str(result))
    for i in list:
        if i == '**' or i == '//':
            looking_for_cube_or_cuberoot(list)


def looking_for_multiply_or_devide(list):
    global used_symbol
    global symbol

    position = 0
    used_symbol = -1
    symbol = "nothing"
    for i in list:
        if i == '*' or i == '/':
            used_symbol = position
            symbol = i
            break
        else:
            symbol = "nothing"
        position += 1
    if symbol == '*':
        multiply(float(list[used_symbol - 1]), float(list[used_symbol + 1]))
        for i in range(used_symbol - 1, used_symbol + 2):
            list.pop(used_symbol - 1)
        list.insert(used_symbol - 1, str(result))
    if symbol == '/':
        devide(float(list[used_symbol - 1]), float(list[used_symbol + 1]))
        for i in range(used_symbol - 1, used_symbol + 2):
            list.pop(used_symbol - 1)
        list.insert(used_symbol - 1, str(result))
    for i in list:
        if i == '*' or i == '/':
            looking_for_multiply_or_devide(list)


def looking_for_plus_or_minus(list):
    global used_symbol
    global symbol

    position = 0
    used_symbol = -1
    symbol = "nothing"
    for i in list:
        if i == '+' or i == '-':
            used_symbol = position
            symbol = i
            break
        else:
            symbol = "nothing"
        position += 1
    if symbol == '+':
        plus(float(list[used_symbol - 1]), float(list[used_symbol + 1]))
        for i in range(used_symbol - 1, used_symbol + 2):
            list.pop(used_symbol - 1)
        list.insert(used_symbol - 1, str(result))
    if symbol == '-':
        minus(float(list[used_symbol - 1]), float(list[used_symbol + 1]))
        for i in range(used_symbol - 1, used_symbol + 2):
            list.pop(used_symbol - 1)
        list.insert(used_symbol - 1, str(result))
    for i in list:
        if i == '+' or i == '-':
            looking_for_plus_or_minus(list)



def deleting_bracket():
    num_list.insert(st_post, bracket_list[0])
    print("Příklad v závorce: " + bracket + " = " + bracket_list[0])
    print("\n")


def calculating_bracket():
    bracket_check()
    if nd_post > -1 and st_post == -1 :
        ("\n")
        print("-----------------------------------------------------------------------------------------------")
        print("Máš chybu v závorkách!")
        print("-----------------------------------------------------------------------------------------------")
        num_of_open_brackets = 0
    print("Závorka nalezena")
    adding_to_bracket_list()
    looking_for_cube_or_cuberoot(bracket_list)
    looking_for_multiply_or_devide(bracket_list)
    looking_for_plus_or_minus(bracket_list)
    deleting_bracket()


def MATH():
    math_problem_check()
    bracket_identifier()
    math_problem_printer()
    if num_of_open_brackets == num_of_close_brackets:
        for i in range(num_of_open_brackets):
            calculating_bracket()
            math_problem_printer()
    bracket_identifier()
    if num_of_open_brackets == 0:
        looking_for_cube_or_cuberoot(num_list)
        looking_for_multiply_or_devide(num_list)
        looking_for_plus_or_minus(num_list)
        math_problem_printer()


MATH()
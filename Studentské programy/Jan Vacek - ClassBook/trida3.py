import random

mates = []

with open("mates.txt", "r") as f:
    txt = f.readlines()
    line = txt[0]
    mates = line.split("_")
    mates.remove("")

# mates = ["Kuba","Eva","Žaneta","Běta","Fanda","Iva","Honza","Aneta","Monča","Katka"]

raw_mates = 4


def round_up(vstup):
    roun = round(vstup)
    if roun < vstup:
        return roun+1
    else:
        return roun


def save():
    with open("mates.txt", "w") as f:
        for i in mates:
            f.write(i + "_")


def help():
    print("help.......for help")
    print("add........for new mates")
    print("v..........for summon mates")
    print("stop.......for exit program")
    print("l..........for list of mates")
    print("k..........for kill one mates")
    print("r..........for choose how many mates is in one row")
    print("KILL ALL...for kill all mates")


def help2():
    print("help                      for help")
    print("add + [student name]      for new mates")
    print("vote_random               for summon random mates")
    print("stop                      for exit program")
    print("show_class                for show class")
    print("kill + [student name]     for kill one mates")
    print("row + [count]             for choose how many mates is in one row")
    print("KILL_ALL                  for kill all mates")


def make_clas():
    count = len(mates)
    rad = count/raw_mates
    mates_last = count % raw_mates
    rad = round_up(rad)

    cl = []

    for i in range(0, rad):
        row = []
        for j in range(0, raw_mates):

            if i == rad - 1 and j == mates_last and mates_last != 0:
                break

            row.append(mates[i*raw_mates + j])

        cl.append(row)

    return cl


def print_clas(cl):
    count = len(mates)
    rad = count/raw_mates
    mates_last = count % raw_mates
    rad = round_up(rad)

    max = 0

    for w in mates:
        number = len(w)
        if(number > max):
            max = number

    max += 2

    print((raw_mates*max+raw_mates+1) * "-")

    for i in range(0, rad):
        for j in range(0, raw_mates):

            if i == rad - 1 and j == mates_last and mates_last != 0:
                break

            printed_word = str(cl[i][j].center(max))

            bef = ""
            aft = ""

            if j == 0 and i * raw_mates + j == count-1:
                bef = "|"
                aft = "|"
            elif j == 0:
                bef = "|"
                aft = " "
            elif j > 0 and j % 2 != 0 or raw_mates-1 == j or i * raw_mates + j == count-1:
                bef = ""
                aft = "|"
            else:
                bef = ""
                aft = " "

            print(bef + printed_word + aft, end='')

        print("")
        print((raw_mates * max + raw_mates+1) * "-")


clas = make_clas()


# while True:
#     n = input("0....Easy\n1....Normal\n: ")
#     if n == "1" or n == "0":
#         n = int(n)
#         break
#     else:
#         print("Try again")

# if(n == 0):
#     print("Welcome in class book for stupid people!!!")
#     help()
# else:
#     print("Welcome in class book!!!")
#     help2()

n = 1
run = True

if(n == 0):
    while run:
        goodComand = False

        comand = input("> ")

        if(comand.lower() == "stop" or comand.lower() == "s"):
            save()
            run = False
            continue

        if(comand.lower() == "help"):
            help()
            continue

        if(comand.lower() == "v"):
            name = ""
            while True:
                rand = random.randint(0, len(mates)-1)
                name = mates[rand]
                if name != "[nobody]":
                    break

            count = len(mates)
            rad = count/raw_mates
            mates_last = count % raw_mates
            rad = round_up(rad)

            for i in range(0, rad):
                for j in range(0, raw_mates):
                    if i == rad - 1 and j == mates_last and mates_last != 0:
                        break

                    if name == clas[i][j]:
                        print(f"{name} [{i}, {j}]")
            continue

        if(comand.lower() == "r"):
            r = input("How many mates do you want in a row: ")
            r = int(r)
            raw_mates = r
            print("Changed!!!")
            clas = make_clas()
            continue

        if(comand.lower() == "add"):
            name = input(
                "What is the new mate's name (if nobody is sitting here write ,nobody,): ")

            if(name == "nobody"):
                name = "[nobody]"
                print("There is nobody!!!")
            else:
                name = name.capitalize()
                print(name + " was added to the hell")

            mates.append(name)
            clas = make_clas()
            continue

        if(comand.lower() == "l"):
            print_clas(clas)
            continue

        if(comand.lower() == "save"):
            save()
            print("Class was saved!")
            continue

        if(comand.lower() == "kill all"):
            mates.clear()
            clas = make_clas()
            continue

        if(comand.lower() == "k"):
            name = input("Which mates do you want to kill: ")
            kill = False

            for i in range(len(mates)):
                if(mates[i].lower() == name.lower()):
                    kill = True
                    print(mates[i] + " was killed!!")
                    mates.remove(mates[i])
                    break

            if(kill == False):
                print("Mates wasn't find, try again")

            clas = make_clas()
            continue

        print("Invalid command. Please use valid command.")

if(n == 1):
    print("Welcome in class book!!!")
    help2()

    while run:
        inp = input(">> ")
        split = inp.split(" ", 1)
        comand = split[0]

        if(comand.lower() == "stop" or comand.lower() == "s"):
            save()
            run = False
            continue

        if(comand.lower() == "add" and len(split) == 2):
            name = split[1]

            if(name == "nobody"):
                name = "[nobody]"
                print("There is nobody!!!")
            else:
                name = name.capitalize()
                print(name + " was added to the hell")
        
            mates.append(name)
            clas = make_clas()
            continue

        if(comand.lower() == "l" or comand.lower() == "show_class" and len(split) == 1):
            print_clas(clas)
            continue

        if(comand.lower() == "help" and len(split) == 1):
            help()
            continue

        if(comand.lower() == "vote_random" or comand.lower() == "v"  and len(split) == 1):
            name = ""
            while True:
                rand = random.randint(0, len(mates)-1)
                name = mates[rand]
                if name != "[nobody]":
                    break
        

            count = len(mates)
            rad = count/raw_mates
            mates_last = count%raw_mates
            rad = round_up(rad)

            for i in range(0, rad):
                for j in range(0, raw_mates):
                    if i == rad - 1 and j == mates_last and mates_last != 0:
                        break
                    
                    if name == clas[i][j]:
                        print(f"{name} [{i}, {j}]")
            continue

        if(comand.lower() == "kill" and len(split) == 2):
            name = split[1]
            kill = False

            for i in range(len(mates)):
                if(mates[i].lower() == name.lower()):
                    kill = True
                    print(mates[i] + " was killed!!")
                    mates.remove(mates[i])
                    break
            
            if(kill == False):
                print("Mates wasn't find, try again")
            
            clas = make_clas()
            continue

        if(comand.lower() == "kill_all" and len(split) == 1):
            mates.clear()
            clas = make_clas()
            continue

        if(comand.lower() == "row" and len(split) == 2):
            r = int(split[1])
            raw_mates = r
            clas = make_clas()
            print("Changed!!!")
            continue

        print("Invalid command. Please use valid command.")


print("See you later my class")

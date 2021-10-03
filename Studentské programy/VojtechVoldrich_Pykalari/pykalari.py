# Made by ostSTRUPpen
# Práce s "databází" a takzvaný user_stupidity manager (neboli help a nakládání s errory)
import programs.file_management as fm
import programs.user_management as um

students_list = fm.load_students()
output = 'Číslo v pořadí: {}\n-Osobní informace: \n--jméno: {}\n--příjmení: {}\n--pohlaví: {}\n--narozeniny(MM/DD/RRRR): {}\n-Bydliště:\n--stát: {}\n--kraj: {}\n--město: {}\n--ulice a číslo popisné: {}\n-Kontakt:\n--email: {}\n--telefoní číslo: {}'


def format_for_console(student):
    return output.format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7], student[8], student[9], student[10])

def reload_student_list():
    global students_list
    students_list = fm.load_students()

# Následující funkce neobsahuje komentáře a doporučuji ji neotvírat
# Důvod je prostý - její vzhled se mi hnusí, ale na druhou stranu jakžtakž funguje, a proto ji nechci měnit
# Dělat něco takového v příkazovém řádku je neefektivní blbost,
# a kdyby to nebylo potřeba pro pořádné předvedení hlavní vymožensti pykalářů, tak ji nevytvářím
def add_student():
    question_num = 0
    input_problem = ''
    student = [len(students_list)+1]
    while True:
        if question_num == 0:
            input_text = input('Křestní jméno studenta? (Ferero)> ').replace(
                ' ', '').capitalize()
            if input_text.isdigit() == False:
                if len(input_text) >= 3:
                    print('Jméno: {} zadáno'.format(input_text))
                    student.append(input_text)
                    question_num += 1
                    continue
                else:
                    input_problem = 'Jméno nemůže být kratší než 3 znaky!'
            else:
                input_problem = 'Jméno nemůže být tvořeno pouze číslicemi!'
            print('Jméno nesplnilo určitý požadavek: {}'.format(input_problem))
        elif question_num == 1:
            input_text = input('Příjmení studenta? (Bonboniery)> ').replace(
                ' ', '').capitalize()
            if input_text.isdigit() == False:
                if len(input_text) >= 3:
                    print('Příjmení: {} zadáno'.format(input_text))
                    student.append(input_text)
                    if input_text.find('ová') == -1 and input_text.find('ova') == -1:
                        student.append('muž')
                    else:
                        student.append('žena')
                    question_num += 1
                    continue
                else:
                    input_problem = 'Příjmení nemůže být kratší než 3 znaky!'
            else:
                input_problem = 'Příjmení nemůže být tvořeno pouze číslicemi!'
            print('Příjmení nesplnilo určitý požadavek: {}'.format(input_problem))
        elif question_num == 2:
            input_text = input(
                'Datum narození studenta? (Měsíc Den Rok např: 9 17 1993)> ')
            if input_text.replace(' ', '').isdigit():
                if len(input_text.replace(' ', '')) >= 6:
                    print('Datum narození: {} zadáno'.format(
                        input_text.replace(' ', '/')))
                    student.append(input_text.replace(' ', '/'))
                    question_num += 1
                    continue
                else:
                    input_problem = 'Datum narození nemůže být kratší než 6 číslic!'
            else:
                input_problem = 'Datum narození musí být tvořeno pouze číslicemi!'
            print('Datum narození nesplnilo určitý požadavek: {}'.format(input_problem))
        elif question_num == 3:
            student.append('Česká republika')
            input_text = input('Název kraje studenta?(Kraj Vysočina)> ').strip()
            if input_text.isdigit() == False:
                if len(input_text.replace(' ', '')) > 5:
                    print('Název kraje: {} zadán'.format(input_text))
                    student.append(input_text)
                    question_num += 1
                    continue
                else:
                    input_problem = 'Název kraje nemůže být kratší než 6 znaků!'
            else:
                input_problem = 'Název kraje nemůže být tvořeno pouze číslicemi!'
            print('Název kraje nesplnil určitý požadavek: {}'.format(input_problem))
        elif question_num == 4:
            input_text = input('Název města studenta? (Havlíčkův Brod)> ').strip()
            if input_text.isdigit() == False:
                if len(input_text.replace(' ', '')) > 5:
                    print('Název města: {} zadán'.format(input_text))
                    student.append(input_text)
                    question_num += 1
                    continue
                else:
                    input_problem = 'Název města nemůže být kratší než 6 znaků!'
            else:
                input_problem = 'Název města nemůže být tvořeno pouze číslicemi!'
            print('Název města nesplnil určitý požadavek: {}'.format(input_problem))
        elif question_num == 5:
            input_text = input(
                'Název ulice a číslo popisné studenta? (Troubov 51)> ').strip()
            test_text = input_text.split(input_text[input_text.rfind(' ')])
            if test_text[0].isdigit() == False and test_text[1].isdigit():
                if len(input_text.replace(' ', '')) >= 5:
                    print('Název ulice a číslo popisné: {} zadáno'.format(input_text))
                    student.append(input_text)
                    question_num += 1
                    continue
                else:
                    input_problem = 'Název ulice a číslo popisné nemůže být kratší než 3 znaky!'
            else:
                input_problem = 'Název ulice nemůže být tvořeno pouze číslicemi a číslo popisné musí být tvořeno pouze číslicemi!'
            print('Název města nesplnil určitý požadavek: {}'.format(input_problem))
        elif question_num == 6:
            input_text = input('Email adresa studenta? (fbonbonieri@seznam.cz)> ').replace(' ','')
            if input_text.find('@') != -1 and input_text.find('.') != -1:
                if len(input_text) >= 5:
                    print('Email adresa: {} zadána'.format(input_text))
                    student.append(input_text)
                    question_num+=1
                    continue
                else:
                    input_problem = 'Email adresa nemůže být kratší než 5 znaků!'
            else:
                input_problem = 'Email adresa musí obsahovat @ a .!'
            print('Email adresa nesplnila určitý požadavek: {}'.format(input_problem))
        elif question_num == 7:
            input_text = input('Telefoní číslo studenta? (396 105 860)> ')
            if input_text.replace(' ','').isdigit():
                if len(input_text.replace(' ','')) == 9:
                    print('Telefoní číslo: {} zadáno'.format(input_text))
                    student.append(input_text)
                    question_num+=1
                    continue
                else:
                    input_problem = 'Telefoní číslo nemůže být kratší než 9 číslic!'
            else:
                input_problem = 'Telefoní číslo musí být tvořeno pouze číslicemi!'
            print('Telefoní číslo nesplnilo určitý požadavek: {}'.format(input_problem))
        elif question_num == 8:
            print(format_for_console(student))
            input_text = input('Mohu zapsat studenta do databáze? (a/n)').lower().strip().replace(' ','')[:1]
            if input_text == 'a':
                print('Ukládám studenta {}'.format(student[0]))
                fm.add_to_file(student)
                reload_student_list()
                print('Student uložen!')
                return
            elif input_text == 'n':
                print('Ruším žádost!')
                return
            else:
                print('Odpověď \'{}\' nezačíná na písmeno \'a\' nebo \'n\' a neodpovídá proto očekávanámu vzorci! \nPtám se proto znovu:'.format(input_text))

# Hlavní číst kódu
print('Pykaláři verze 1.0.0')
print('Napište help pro zobrazení všech příkazů')
while True:
    # Zpracování vstupu
    # Rozdělení na příkaz a argumenty
    # Úprava příkazu a lstu argumentů
    inputString = input('> ')
    inputString += ' '
    command = inputString[:inputString.index(' ')].lower()
    args = inputString[inputString.index(
        ' '):].lower().replace(' ', '').split('-')
    args.pop(0)
    # Commands manager
    if command == 'help':
        if args == []:
            print(um.help('all'))
        elif args[0] == '?':
            print(um.help(command))
        else:
            print(um.handle(2, command, args))
    elif command == 'exit':
        if args == []:
            exit()
        elif args[0] == '?':
            print(um.help(command))
        else:
            print(um.handle(2, command, args))
    elif command == 'list':
        if args == []:
            print(um.handle(1, command, args))
        elif args[0] == '?':
            print(um.help(command))
        elif args[0] == 'a':
            for student in students_list:
                print(format_for_console(student))
        elif args[0] == 'l':
            print(len(students_list))
        elif args[0].isdigit() == True:
            if int(args[0]) <= 0:
                print(um.handle(300, command, args))
            elif int(args[0]) >= len(students_list)+1:
                print(um.handle(301, command, args) + str(len(students_list)))
            else:
                student = students_list[int(args[0])-1]
                print(format_for_console(student))
        else:
            print(um.handle(2, command, args))
    elif command == 'del':
        if args == []:
            print(um.handle(1, command, args))
        elif args[0] == '?':
            print(um.help(command))
        elif args[0].isdigit() == True:
            if int(args[0]) <= 0:
                print(um.handle(400, command, args))
            elif int(args[0]) >= len(students_list)+1:
                print(um.handle(401, command, args) + str(len(students_list)))
            else:
                print(format_for_console(students_list[int(args[0])-1]))
                sure = input('Určitě chcete odstranit studenta z databáze? (a/n)> ').lower().strip().replace(' ','')[:1]
                if sure == 'a':
                    print('Mažu studenta ' + args[0])
                    fm.delete_in_file(args[0])
                    reload_student_list()
                    print('Hotovo')
                elif sure == 'n':
                    print('Ruším žádost!')
                else:
                    print(um.handle(402, sure, []))
        else:
            print(um.handle(2, command, args))
    elif command == 'add':
        if args == []:
            add_student()
        elif args[0] == '?':
            print(um.help(command))
        else:
            print(um.handle(2, command, args))
    else:
        print(um.handle(0, command, args))

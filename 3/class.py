

classroom = ['Adam', 'Pepa', 'David', 'Jonas']


# i = 0
# while i < 4:
#     print(str(i+1) + '. - ' + classroom[i])
#     i = i+1

command = 'help'
while True:
    # Next command
    command = input('What do you want?')

    if command.lower() == 'exit':
        print('Goodbye:...')
        break

    if command.lower() == 'list_while':
        i = 0
        while i < 4:
            print(str(i+1) + '. - ' + classroom[i])
            i = i+1

    #list_range
    if command.lower() == 'list':
        for i in range(len(classroom)):
            print(str(i+1) + '. - ' + classroom[i])

    if command.lower() == 'list_all':
        for student in classroom:
            print(student)

    if command == 'help':
        print('Toto je help:')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')



    command_list = command.split(' ', 1)
    # print(len(command_list))
    if len(command_list)<2:
        continue
    
    # print('Co je v command listu:')
    # print(command_list)
    command = command_list[0]
    new_student = command_list[1]

    # add student
    if command.lower() == 'add':
        classroom.append(new_student)
        print(command_list[1] + ' was added to the classroom.')


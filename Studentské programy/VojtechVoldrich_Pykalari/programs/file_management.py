# Made by ostSTRUPpen
# Práce se soubory
def read_file():
    with open('data\\students.txt', 'r',  encoding="utf8") as file:
        return file.read()

def rewrite_file(text):
    with open('data\\students.txt', 'w',  encoding="utf8") as file:
        write_text = ''
        for line in text:
            text_line = ''
            for part in line:
                text_line += '|' + str(part)
            text_line = text_line[1:]
            write_text += '\n' + str(text_line)
        write_text = write_text[1:]
        file.write(write_text)

def append_file(text):
     with open('data\\students.txt', 'a',  encoding="utf8") as file:
         file.write(text)
# Přechod mezi programem a soubory
def load_students():
    students = []
    students_lines_list = read_file().split('\n')
    students_lines_list.pop(0)
    for student in students_lines_list:
        student_prov = student.split('|')
        students.append(student_prov)
    return students

def delete_in_file(id):
    old_file = read_file().split('\n')
    new_file = []
    for i in range(len(old_file)):
        student = old_file[i].split('|')
        if student[0] == id:
            old_file.pop(i)
            break
    new_file.append(old_file[0].split('|'))
    for i in range (1,len(old_file)):
        student = old_file[i].split('|')
        new_student = [i, student[1], student[2], student[3], student[4],student[5], student[6], student[7], student[8], student[9], student[10]]
        new_file.append(new_student)
    rewrite_file(new_file)

def add_to_file(text):
    append_text = ''
    text_line = ''
    for part in text:
        append_text += '|' + str(part)
    append_text = append_text[1:]
    append_text = '\n' + str(append_text)
    append_file(append_text)



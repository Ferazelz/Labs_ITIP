groupmates = [
    {
        "name": "Александр",
        "surname": "Есин",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Александр",
        "surname": "Сытов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Захар",
        "surname": "Дорофеев",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Сергей",
        "surname": "Филин",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 4]
    },
{
        "name": "Ростислав",
        "surname": "Лебедев",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 5]
    },
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
        
def print_students_average_filter(students, average):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        if(averageCheck(student["marks"])>float(average)):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
        
def averageCheck(marks):
    averResult = 0
    for mark in marks:
        averResult = averResult + mark
    return averResult/len(marks)

    
print (u"\nВывод списка студентов:")
print_students(groupmates)

print (u"\nВведите средний бал для фильтрации студентов:")
average = input().replace(',', '.')
print_students_average_filter(groupmates, average)

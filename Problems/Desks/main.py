# put your python code here
class1_number_of_students = int(input())
class2_number_of_students = int(input())
class3_number_of_students = int(input())


def get_desk_numbers(number_of_students):
    return number_of_students // 2 if number_of_students % 2 == 0 else (number_of_students + 1) // 2


class1_desks = get_desk_numbers(class1_number_of_students)
class2_desks = get_desk_numbers(class2_number_of_students)
class3_desks = get_desk_numbers(class3_number_of_students)

print(class1_desks + class2_desks + class3_desks)





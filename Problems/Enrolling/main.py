dict_anne = {"name": "Anne", "average_grade": 49, "recommended_by_tutor": True, "finished_introductory_course": False,
             "introductory_course_grade": 0}
dict_john = {"name": "John",
             "average_grade": 41,
             "recommended_by_tutor": False,
             "finished_introductory_course": True,
             "introductory_course_grade": 76}
dict_frank = {"name": "Frank",
              "average_grade": 37,
              "recommended_by_tutor": True,
              "finished_introductory_course": True,
              "introductory_course_grade": 97}
dict_victoria = {"name": "Victoria",
                 "average_grade": 40,
                 "recommended_by_tutor": True,
                 "finished_introductory_course": True,
                 "introductory_course_grade": 86}
dict_mary = {"name": "Mary", "average_grade": 49,
             "recommended_by_tutor": False,
             "finished_introductory_course": True,
             "introductory_course_grade": 85}
dict_sam = {"name": "Sam", "average_grade": 33,
            "recommended_by_tutor": False,
            "finished_introductory_course": True,
            "introductory_course_grade": 51}

all_data = [dict_anne, dict_john, dict_frank, dict_victoria, dict_mary, dict_sam]

for student in all_data:
    enroll_student = ((student['average_grade'] >= 40 and student['recommended_by_tutor'])
                      or (student['finished_introductory_course'] and student['introductory_course_grade'] > 85))
    if enroll_student:
        print(student['name'])

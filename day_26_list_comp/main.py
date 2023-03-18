student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.student)
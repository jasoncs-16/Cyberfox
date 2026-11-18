import json

with open("dataset.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)


def average_grades(dataset):
    names = dataset["students"]
    all_student_grades = dataset["grades"]
    averaging_list = []

    for student_grades in all_student_grades:
        total = sum(student_grades)
        media = total / len(student_grades)
        averaging_list.append(round(media, 2))

    return [names, averaging_list]


print(average_grades(dataset))
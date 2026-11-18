import json

with open("dataset.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)


def average_grades(dataset):
      """Calculates the average for each student based on their 5 grades."""
    names = dataset["students"]
    all_student_grades = dataset["grades"]
    averaging_list = []
	  # Recorremos cada lista de notas correspondiente a un alumno
    for student_grades in all_student_grades:
        total = sum(student_grades)
        media = total / len(student_grades)
        averaging_list.append(round(media, 2))
	 # Devolvemos la estructura lista para tu función de filtrado
    return [names, averaging_list]


print(average_grades(dataset))
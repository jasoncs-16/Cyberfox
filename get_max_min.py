def get_max_min(dateset: list) -> list:
    max = 0
    min = 0
    grades = []
    for list in dateset:
        for element in list:
            if element > max:
                max = element
            if element < min:
                min = element
        grades.append(max, min)
    return grades

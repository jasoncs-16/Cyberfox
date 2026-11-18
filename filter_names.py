def filter_passed(data):
    """
    Classifies students into those who passed and those who need extraordinary exams. 
        Args: 
            data (list of lists): A list where data[0] is a list of student names (str) and data[1] is a list of corresponding grades (float/int). 
        Returns: 
            tuple: Two lists (passed_names, extraordinary_names) separating the students based on whether their grade is >= 5.0 or < 5.0. 
    """

    # Separate the main nested list into names (index 0) and grades (index 1) 
    names = data[0] 
    grades = data[1] 
    passed_names = [] 
    extraordinary_names = []
    # Iterate through both lists in parallel to evaluate if each student passed (>= 5.0)
    for name, grade in zip(names, grades):
        if grade >= 5.0: 
            passed_names.append(name) 
        else: 
            extraordinary_names.append(name)
    return passed_names, extraordinary_names

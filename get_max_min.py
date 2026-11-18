def get_max_min(dataset: list) -> list:
    """Returns [(max_name, max_grade), (min_name, min_grade)]."""
    names, grades = dataset

    # If there is no data, we avoid errors
    if not names or not grades:
        return [(None, 0), (None, 0)]

    max_val, min_val = float("-inf"), float("inf")
    max_name = min_name = None

    for name, student_grades in zip(names, grades):
        for grade in student_grades:
            if grade > max_val:
                max_val, max_name = grade, name
            if grade < min_val:
                min_val, min_name = grade, name

    return [(max_name, max_val), (min_name, min_val)]

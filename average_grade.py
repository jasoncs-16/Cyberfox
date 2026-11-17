def average_grades(dateset):
	"""
	 average grades of students
	Args:
	dataset(strings and floats) : a list of lists that have one list of names of the students and another list of floats.

	Returns:
		the average (float) of each student.
	"""
	
    
	lista = []
	for lista in data[1]:
		for grades in lista:
			media += grades 
			media = media / len(lista)
	lista.append(media)
	return lista

file_path = 'C:\\Users\\Johnson\\Documents\\PythonPlayground\\Basic\\pi_digits.txt'
with open(file_path) as file_object:

 pi_string = ""
 for line in file_object:
 	pi_string += line.strip()
 	
 print(pi_string)
name = ""
age = 0
ocuppation = ""
department = ""


def start():
	value = 5 * 2 + 2 * (2 ** 4 - 4) / 2

	ask_salary()


def welcome():
	print("Welcome to the Data Science class")


def ask_name():
	global name
	name = input("Type the name ")
	print("Your name was saved")

def ask_age():
	global age

	try:
		age = int(input("Type the age "))
	except:
		print("You typed wrong value, try to type a number")

	print("Your age was saved")
	

def ask_occupation():
	global occupation
	occupation = input("Type the occupation ")
	print("Your occupation was saved")


def ask_department():
	global department
	department = input("Type your department ")


def ask_person_data():
	ask_name()
	ask_age()
	ask_occupation()
	ask_department()	


def ask_car():
	global car
	car = input("Type the name of your car ")


def ask_car_engine():
	global car_engine
	car_engine = float(input("Type the engine liter of your car "))


def ask_car_doors():
	global car_doors
	car_doors = int(input("Type the number of doors that your car has "))


def ask_car_data():
	ask_car()
	ask_car_engine()
	ask_car_doors()

	print(type(car), type(car_engine), type(car_doors))


def ask_course():
	global course_name
	course_name = input("Type the name of your course ")


def ask_salary():
	global salary
	global new_salary

	salary = float(input("Type your salary "))

	new_salary = salary * 1.15

	print(f"salary: {salary}. new salary: {new_salary:.3f} {new_salary:.2f} {new_salary:.1f} {new_salary:.0f} ")






def print_course_data():
	global course_name
	print(f"\n The course name is: \n{course_name}")


def print_data():
	print("Your name is: ", name, "Your age is: ", age, "The occupation is: ", occupation, "The department is: ", department)
	print(type(name))
	print(type(age))
	print(type(occupation))
	print(type(department))



start()


"""
calculator
+ soma
- subtração
* multiplicação
/ divisão
// divisão inteira
% resto da divisão
** potência
"""
def my_sum(value_one, value_two):
	return value_one + value_two


def my_subtract(value_one, value_two):
	return value_one - value_two


def my_multiply(value_one, value_two):
	return value_one * value_two


def my_divide(value_one, value_two):
	return value_one * value_two


def my_divide_without_rest(value_one, value_two):
	return value_one // value_two


def my_rest(value_one, value_two):
	return value_one % value_two


def my_potential(value_one, value_two):
	return value_one ** value_two


def calculator():
	operations_text = f"+,  -,  /,  *, //, % or **"
	print(f"Welcome to the calculator")
	print(f"You should type a number")
	print(f"Then you should type the operation {operations_text}")
	print(f"And the you type the second number")

	number_one = float(input("Type the first number "))
	operation = input(f"Type the operation {operations_text}")
	number_two = float(input("Type the second number "))

	
	
	if operation == "+":
		result = number_one + number_two
	elif operation == "-":
		result = number_one - number_two
	elif operation == "*":
		result = number_one * number_two
	elif operation == "/":
		result = number_one / number_two
	elif operation == "//":
		result = number_one // number_two
	elif operation == "%":
		result = number_one % number_two

	print(result)
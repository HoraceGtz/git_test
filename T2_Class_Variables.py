#Linea de código cambiada para prueba de subir a github
#Variables de clase: aquellas que se comparten entre todas las instacias de una clase

class Employee:

	#Contador de empleados
	num_of_emps=0

	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@compay.com"

		#Ya que se ejecuta cada vez que creamos un empleado
		Employee.num_of_emps +=1

	def fullname(self):
				
		return  "{} {}".format(self.first, self.last)

	
	#Manualmente 
	#Aumento de 4%	
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount )


emp_1= Employee("Corey", "Schafer", 50000)
emp_2= Employee("Test", "User", 60000  )

print("Tasa de aumento = ", Employee.raise_amount)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#Sobre emp_1
print(emp_1.__dict__)

#Modificando variable de clase
Employee.raise_amount = 1.05
emp_1.apply_raise = 2.0

#De clase
print("Tasa de aumento = ", Employee.raise_amount)
#De instancia (especifico)
print("Tasa de aumento = ", emp_1.apply_raise)

####
print("\nNúmero de empleados: ",Employee.num_of_emps)
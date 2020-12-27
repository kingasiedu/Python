# create this sample class that uses encapsulation and class methods

class Employee:
    # Private variables and methods names should be preceded with __ (two underscores)
    __hourly_rate = None
    __weekly_hours = None
    __last_name = None
    __first_name = None

    def __init__(self, l, f, h, w):
        self.__hourly_rate = h
        self.__weekly_hours = w
        self.__last_name = l
        self.__first_name = f

    def setLastName(self, last_name):
        self.__last_name = last_name

    def getLastName(self):
        return self.__last_name

    def setFirstName(self, first_name):
        self.__first_name = first_name

    def getFirstName(self):
        return self.__first_name

    def setHourlyRate(self, rate):
        self.__hourly_rate = rate

    def getHourlyRate(self):
        return self.__hourly_rate

    def setWeeklyHours(self, hrs):
        self.__weekly_hours = hrs

    def getWeeklyHours(self):
        return self.__weekly_hours

    def calcWeeklySalary(self):
        return self.__weekly_hours * self.__hourly_rate

    @classmethod
    def baseEmployeeFactory(cls, last_name, first_name):
        return cls(last_name, first_name, 15.00, 40)


emp1 = Employee("Doe", "John", 12.50, 40)
emp2 = Employee.baseEmployeeFactory("Doe", "Jane")
print("emp1 weekly salary %0.2f vs emp2 weekly salary %0.2f" % (emp1.calcWeeklySalary(), emp2.calcWeeklySalary()))

last_name_list = ["Jones", "Smith", "Williams", "Johnson", "Brown", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]
first_name_list = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William",
                   "Elizabeth"]
salary_list = [2400, 488, 3400, 400, 450, 5899, 475, 200, 5889, 5899, 553, 793, 3009, 3900, 9884, 694, 2890]


class SalaryEmployees(Employee):
    def __init__(self, l, f, salary):
        super().__init__(l, f, 0, 0, )
        __weekly_salary = None
        self.__weekly_salary = salary

    def setWeeklySalary(self, salary):
        self.__weekly_salary = salary

    @classmethod
    def baseEmployeeFactory(cls, last_name, first_name):
        return cls(last_name, first_name, 2500)

    def calcWeeklySalary(self):
        return self.__weekly_salary


import random


def rand_employees():
    for i in range(0, 10, 1):
        last = random.choice(last_name_list)
        first = random.choice(first_name_list)
        salary = random.choice(salary_list)
        emp = SalaryEmployees(first, last, salary)

        print("%s %s salary %0.2f" %
              (emp.getFirstName(), emp.getLastName(), emp.calcWeeklySalary()))


rand_employees()

baseFactory = SalaryEmployees.baseEmployeeFactory(" Asiedu", "Kingsley")
print("%s %s salary %0.2f" %
        (baseFactory.getFirstName(), baseFactory.getLastName(), baseFactory.calcWeeklySalary()))

# can you write a class SalaryEmployee that:
# inherits from Employee
# implements employees paid a salary instead of hourly wage
# -- override __init__ with a class that includes a base weekly salary value as __weekly_salary
# -- override calcWeeklySalary to return the value of __weekly_salary
# -- create new instance method setWeeklySalary() that sets the value of __weekly_salary
# -- override baseEmployeeFactory to return a class instance with a base salary of 2500
# can you write a method to generate a list of ten random SalaryEmployees using last_name_list, first_name_list, and
# salary_list?

class Employee:
    full_names = [['Ivan','Ivanov'],['Vitya','Loshkin'],['Lev','Tolstoj']]
    departments = ['hr','base','space']
    def __init__(self,name,surname,department,year):
        try:
            self.check_name = False
            self.check_year = False
            self.check_department = False
            self.name = name
            self.surname = surname
            self.year = int(year)
            self.full_name = [[self.name,self.surname],[0,1]]
            self.department = department
            for i in Employee.full_names:
                if self.full_name[0] == i:
                    self.check_name=True
            if self.year >= 2002:
                self.check_year = True
            for j in Employee.departments:
                if self.department == j:
                    self.check_department = True
            if self.check_year == False:
                print('Год не верен')
            if self.check_department == False:
                print('Такого отдела не существует')
            if self.check_name == False:
                print('Данный сотрудник у нас не числится')
            if (self.check_name and self.check_year and self.check_department):
                print('Добро пожаловать в систему {}'.format(self.full_name[0]))
        except BaseException as error:
            print('Exception666:', error.with_traceback(None))
            print('Введите год цифрами')


a = Employee('Ivan','Ivanov','hr','2006')
b = Employee('Vitya','Loshkin','base','2000')
c = Employee('Petya','Grishin','plot','asd')
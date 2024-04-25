class Worker:
    def __init__(self, name, position, salary):
        self._name = name
        self._position = position
        self._salary = salary

    def __str__(self):
        return f'Name: {self.name}, Position: {self.position}, Salary: {self.salary}'

    @property
    def name(self):
        return self._name
    
    @property
    def position(self):
        return self._position
    
    @property
    def salary(self):
        return self._salary
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @position.setter
    def position(self, new_position):
        self._position = new_position

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

if __name__ == '__main__':
    employee = Worker('John', 'janitor', 1_000_000)
    print(employee.__str__())
        
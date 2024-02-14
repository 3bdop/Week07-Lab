class Employee:
    def __init__(self, name, age, id, department) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.department = department
        
    def setName(self, name):
        self.name = name
        
    def setAge(self, age):
        self.age = age
        
    def setId(self, id):
        self.id = id
        
    def getId(self):
        return self.id
        
    def setDepartment(self, department):
        self.department = department
        
class EMS:
    def __init__(self) -> None:
        self.employeeList = []
        
    def addNewEmployee(self, name, age, id, department):
        self.employeeList.append({Employee(name, age, id, department)})
        

x = EMS()

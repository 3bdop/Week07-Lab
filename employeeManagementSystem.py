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

    def setDepartment(self, department):
        self.department = department

    def getId(self):
        return self.id

    def getAge(self):
        return self.age

    def getDepartment(self):
        return self.department

    def __str__(self) -> str:
        return f"Employee ID: {self.id}\n Employee Name: {self.name}\n Employee Age:{self.age}\n Employee Department: {self.department}"

    # Inside the Employee class definition
    def __eq__(self, other):
        if isinstance(other, Employee):
            return (self.name, self.age, self.id, self.department) == (
                other.name,
                other.age,
                other.id,
                other.department,
            )
        return False


class EMS:
    def __init__(self) -> None:
        self.employeeList = []

    def addNewEmployee(self, name, age, department):
        self.employeeList.append(
            Employee(name, age, len(self.employeeList) + 1, department)
        )

    def getEmployeeInfo(self, id):
        for i in self.employeeList:
            if id == i.getId():
                return i

    def deleteEmployeeInfo(self, id):
        for i in self.employeeList:
            if id == i.getId():
                self.employeeList.remove(i)


def main():
    obj = EMS()
    while True:
        print("Choose one of the following options:")
        inpt = input(
            "\tType 1 for adding new employee\n\tType 2 for getting an employee by the ID\n\tType 3 for deleting an employee by the ID\n\tType q to quit: "
        ).replace(" ", "")

        if inpt == "1":
            name = input("Enter the employee name: ")
            age = input("Enter the employee age: ")
            dpt = input("Enter the employee department: ")
            if not (name.isalpha() and age.isdigit() and dpt.isalpha()):
                print("\nPlease check your input\n")
                continue
            if int(age) < 19:
                print("\nAge must be at least 20\n")
                continue
            obj.addNewEmployee(name, int(age), dpt)
            print("\nA new employee have been added succefully!")
            print("\n---------------------------------------------\n")

        if inpt == "2":
            id = input("Enter the employee ID: ")
            if id.isalpha() or id == "":
                print("\nPlease check your input\n")
                continue
            res = obj.getEmployeeInfo(int(id))
            if res == None:
                print("\nThere is no employee with that ID\n")
                continue
            print("\n", res)
            print("\n---------------------------------------------\n")

        if inpt == "3":
            id = input("Enter the employee ID: ")
            res = obj.deleteEmployeeInfo(int(id))
            if res == None:
                print("\nThere is no employee with that ID\n")
                continue
            print("\nEmployee succefully deleted!")
            print("\n---------------------------------------------\n")

        if inpt == "q":
            break


if __name__ == "__main__":
    main()

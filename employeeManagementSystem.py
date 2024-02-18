class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getID(self):
        return self.id

    def getDepartment(self):
        return self.department

    def __str__(self):
        return f"Employee id: {self.getID()}\nName: {self.getName()}\nAge: {self.getAge()}\nDepartment: {self.getDepartment()}"

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

    def addNewEmployee(self, id, name, age, department):
        if not id.isdigit():
            raise ValueError("ID must be a valid integer")
        if int(id) <= 0:
            raise ValueError("ID must be a positive integer greater than 0")

        for i in self.employeeList:
            if int(id) == i.getID():
                raise ValueError("ID already exists")

        if not name.isalpha():
            raise ValueError("Invalid name")
        if not age.isdigit():
            raise ValueError("Age must be a valid integer")
        if not (20 <= int(age) < 70):
            raise ValueError("Age must be between 20 and 60")
        if department.lower().strip() not in [
            "it",
            "human resources",
            "marketing",
            "training and development",
            "finance",
            "public relations",
        ]:
            raise ValueError("Invalid department")
        self.employeeList.append(
            Employee(name.strip(), int(age), int(id), department.strip().upper())
        )

    def getEmployeeInfo(self, id):
        if not id.isdigit():
            raise ValueError("invalid ID")
        for i in self.employeeList:
            if int(id) == i.getID():
                return i
        raise ValueError(f"ID: {id} does not exist")

    def deleteEmployeeInfo(self, id):
        if not id.isdigit():
            raise ValueError("invalid ID")
        for i in self.employeeList:
            if int(id) == i.getID():
                self.employeeList.remove(i)
                return
        raise ValueError(f"ID: {id} does not exist")


def main():
    obj = EMS()
    while True:
        try:
            print("Choose one of the following options:")
            inpt = input(
                "\tType 1 for adding new employee\n\tType 2 for getting an employee by the ID\n\tType 3 for deleting an employee by the ID\n\tType q to quit: "
            ).replace(" ", "")

            if inpt == "1":
                id = input("Enter the employee ID: ")
                name = input("Enter the employee name: ")
                age = input("Enter the employee age: ")
                dpt = input("Enter the employee department: ")

                obj.addNewEmployee(id, name, age, dpt)
                print("\nA new employee have been added succefully!")
                print("\n---------------------------------------------\n")

            if inpt == "2":
                id = input("Enter the employee ID: ")
                res = obj.getEmployeeInfo(id)

                print("\n", res)
                print("\n---------------------------------------------\n")

            if inpt == "3":
                id = input("Enter the employee ID: ")
                res = obj.deleteEmployeeInfo(id)

                print("\nEmployee succefully deleted!")
                print("\n---------------------------------------------\n")

            if inpt == "q":
                break

        except ValueError as e:
            print()
            print(e)
            print("Please try again.")
        except Exception as e:
            print("\nAn unexpected error occurred:", e)
            print("Please try again.")


if __name__ == "__main__":
    main()
